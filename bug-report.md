Title: Open Redirect vulnerability in /redirect endpoint
Description:
The application is vulnerable to Unvalidated Redirects and Forwards (Open Redirect) on the /redirect endpoint. The to parameter does not sufficiently validate or sanitize user input. An attacker can intercept and modify this parameter to redirect victims to arbitrary external domains, bypassing the intended redirection logic.
Steps to Reproduce:
Configure the browser to route traffic through Burp Suite.
Navigate to the target application (http://localhost:3000).
Trigger an action that uses the redirect endpoint, or manually access: http://localhost:3000/redirect?to=[https://github.com/bkimminich/juice-shop](https://github.com/bkimminich/juice-shop)
Intercept the HTTP request in Burp Suite Proxy.
Modify the to parameter to an external, attacker-controlled domain (e.g., to=[http://evil.com](http://evil.com) or to=[http://google.com](http://google.com)).
Forward the request.
Observe that the application successfully redirects the user to the modified external URL.
Impact:
This vulnerability can be heavily exploited in phishing campaigns. Attackers can craft malicious links that appear to belong to the trusted localhost:3000 domain. When users click the link, they are redirected to a malicious site designed to steal credentials or distribute malware, leveraging the trust of the original domain.
Remediation:
Avoid using user-supplied input directly for redirects.
If dynamic redirects are necessary, implement a strict server-side allowlist of approved URLs.
Alternatively, use indirect references (e.g., ?to=1 redirects to GitHub, ?to=2 redirects to Twitter) mapped securely on the backend.
