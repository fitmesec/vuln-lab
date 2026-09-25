# Сводка скана ZAP: http://juice-shop:3000

Исходный отчёт: `juice-baseline.json`

## Итого

| Уровень риска | Типов находок | Срабатываний |
|---|---|---|
| High | 1 | 1 |
| Medium | 4 | 16 |
| Low | 7 | 29 |
| Informational | 5 | 15 |

## Находки по приоритету

### 1. [High] Off-site Redirect

- Срабатываний: 1
- CWE: 601
- Пример: `http://juice-shop:3000/redirect?to=https://github.com/juice-shop/juice-shop`
- Как исправить: To avoid the open redirect vulnerability, parameters of the application script/program must be validated before sending 302 HTTP code (redirect) to the client browser. Implement safe redirect functionality that only redirects to relative URI's, or a list of trusted domains.

### 2. [Medium] Content Security Policy (CSP) Header Not Set

- Срабатываний: 5
- CWE: 693
- Пример: `http://juice-shop:3000`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### 3. [Medium] Session ID in URL Rewrite

- Срабатываний: 5
- CWE: 598
- Пример: `http://juice-shop:3000/socket.io/?EIO=4&transport=polling&t=Q3OH3Sb&sid=PCq34YW2gxD4ssa2AAAG`
- Как исправить: For secure content, put session ID in a cookie. To be even more secure consider using a combination of cookie and URL rewrite.

### 4. [Medium] Cross-Domain Misconfiguration

- Срабатываний: 3
- CWE: 264
- Пример: `http://juice-shop:3000`
- Как исправить: Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance). Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

### 5. [Medium] Missing Anti-clickjacking Header

- Срабатываний: 3
- CWE: 1021
- Пример: `http://juice-shop:3000/socket.io/?EIO=4&transport=polling&t=Q3OH3Sa&sid=PCq34YW2gxD4ssa2AAAG`
- Как исправить: Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app. If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

### 6. [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid

- Срабатываний: 5
- CWE: 693
- Пример: `http://juice-shop:3000`
- Как исправить: Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents. If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

### 7. [Low] Cross-Origin-Opener-Policy Header Missing or Invalid

- Срабатываний: 5
- CWE: 693
- Пример: `http://juice-shop:3000`
- Как исправить: Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents. 'same-origin-allow-popups' is considered as less secured and should be avoided. If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

### 8. [Low] Deprecated Feature Policy Header Set

- Срабатываний: 5
- CWE: 16
- Пример: `http://juice-shop:3000`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header instead of the Feature-Policy header.

### 9. [Low] Timestamp Disclosure - Unix

- Срабатываний: 5
- CWE: 497
- Пример: `http://juice-shop:3000/styles.css`
- Как исправить: Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

### 10. [Low] X-Content-Type-Options Header Missing

- Срабатываний: 5
- CWE: 693
- Пример: `http://juice-shop:3000/socket.io/?EIO=4&transport=polling&t=Q3OH3Sb&sid=PCq34YW2gxD4ssa2AAAG`
- Как исправить: Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages. If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### 11. [Low] Dangerous JS Functions

- Срабатываний: 3
- CWE: 749
- Пример: `http://juice-shop:3000/about.component-CZcG2819.js`
- Как исправить: See the references for security advice on the use of these functions.

### 12. [Low] Private IP Disclosure

- Срабатываний: 1
- CWE: 497
- Пример: `http://juice-shop:3000/rest/admin/application-configuration`
- Как исправить: Remove the private IP address from the HTTP response body. For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.

### 13. [Informational] Modern Web Application

- Срабатываний: 5
- Пример: `http://juice-shop:3000`
- Как исправить: This is an informational alert and so no changes are required.

### 14. [Informational] Storable but Non-Cacheable Content

- Срабатываний: 5
- CWE: 524
- Пример: `http://juice-shop:3000`
- Как исправить: нет рекомендации

### 15. [Informational] Non-Storable Content

- Срабатываний: 3
- CWE: 524
- Пример: `http://juice-shop:3000/ftp/coupons_2013.md.bak`
- Как исправить: The content may be marked as storable by ensuring that the following conditions are satisfied: The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable) The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood) The "no-store" cache directive must not appear in the request or response header fields For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives) In addition to the conditions above, at least one of the following conditions must also be satisfied by the response: It must contain an "Expires" header field It must contain a "max-age" response directive For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive It must contain a "Cache Control Extension" that allows it to be cached It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).

### 16. [Informational] Information Disclosure - Information in Browser sessionStorage

- Срабатываний: 1
- CWE: 359
- Пример: `http://juice-shop:3000/#/basket`
- Как исправить: This is an informational alert and no action is necessary.

### 17. [Informational] Storable and Cacheable Content

- Срабатываний: 1
- CWE: 524
- Пример: `http://juice-shop:3000/robots.txt`
- Как исправить: Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user: Cache-Control: no-cache, no-store, must-revalidate, private Pragma: no-cache Expires: 0 This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.
