"""
zap_parser.py — превращает JSON-отчёт OWASP ZAP в понятную сводку в Markdown.

Запуск:
    python3 zap_parser.py reports/dvwa-baseline.json
"""

import json
import re
import sys
from pathlib import Path

# ZAP хранит уровень риска числом. Переводим в слова.
RISK_NAMES = {3: "High", 2: "Medium", 1: "Low", 0: "Informational"}


def clean_html(text):
    """Убирает HTML-теги (<p>, <br> и т.п.), которые ZAP вставляет в тексты."""
    text = re.sub(r"<[^>]+>", " ", text or "")
    return " ".join(text.split())


def load_alerts(report_path):
    """Читает JSON-отчёт ZAP и возвращает цель скана и список находок."""
    with open(report_path, encoding="utf-8") as f:
        report = json.load(f)

    target = "неизвестно"
    alerts = []
    for site in report.get("site", []):
        target = site.get("@name", target)
        for alert in site.get("alerts", []):
            instances = alert.get("instances", [])
            alerts.append({
                "name": alert.get("name", "Без названия"),
                "risk": int(alert.get("riskcode", 0)),
                "count": int(alert.get("count", len(instances))),
                "cwe": alert.get("cweid", ""),
                "example_url": instances[0].get("uri", "") if instances else "",
                "solution": clean_html(alert.get("solution", "")),
            })

    # Сначала самое опасное; внутри одного уровня — где больше срабатываний.
    alerts.sort(key=lambda a: (-a["risk"], -a["count"]))
    return target, alerts


def build_markdown(target, alerts, source_name):
    """Собирает текст сводки в формате Markdown."""
    lines = [
        f"# Сводка скана ZAP: {target}",
        "",
        f"Исходный отчёт: `{source_name}`",
        "",
        "## Итого",
        "",
        "| Уровень риска | Типов находок | Срабатываний |",
        "|---|---|---|",
    ]
    for code in (3, 2, 1, 0):
        group = [a for a in alerts if a["risk"] == code]
        total = sum(a["count"] for a in group)
        lines.append(f"| {RISK_NAMES[code]} | {len(group)} | {total} |")

    lines += ["", "## Находки по приоритету", ""]
    for number, a in enumerate(alerts, start=1):
        lines.append(f"### {number}. [{RISK_NAMES[a['risk']]}] {a['name']}")
        lines.append("")
        lines.append(f"- Срабатываний: {a['count']}")
        if a["cwe"] and a["cwe"] != "-1":
            lines.append(f"- CWE: {a['cwe']}")
        if a["example_url"]:
            lines.append(f"- Пример: `{a['example_url']}`")
        lines.append(f"- Как исправить: {a['solution'] or 'нет рекомендации'}")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Использование: python3 zap_parser.py <путь к JSON-отчёту>")
        sys.exit(1)

    report_path = Path(sys.argv[1])
    target, alerts = load_alerts(report_path)
    markdown = build_markdown(target, alerts, report_path.name)

    output_path = report_path.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Готово: {output_path} (типов находок: {len(alerts)})")


if __name__ == "__main__":
    main()
