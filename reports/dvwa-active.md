# Сводка скана ZAP: http://dvwa

Исходный отчёт: `dvwa-active.json`

## Итого

| Уровень риска | Типов находок | Срабатываний |
|---|---|---|
| High | 0 | 0 |
| Medium | 9 | 49 |
| Low | 16 | 72 |
| Informational | 15 | 61 |

## Находки по приоритету

### 1. [Medium] Application Error Disclosure

- Срабатываний: 14
- CWE: 550
- Пример: `http://dvwa/README.ar.md`
- Как исправить: Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.

### 2. [Medium] Source Code Disclosure - SQL

- Срабатываний: 13
- CWE: 540
- Пример: `http://dvwa/README.ar.md`
- Как исправить: Ensure that application Source Code is not available with alternative extensions, and ensure that source code is not present within other files or data deployed to the web server, or served by the web server.

### 3. [Medium] Absence of Anti-CSRF Tokens

- Срабатываний: 5
- CWE: 352
- Пример: `http://dvwa/vulnerabilities/captcha/`
- Как исправить: Phase: Architecture and Design Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, use anti-CSRF packages such as the OWASP CSRFGuard. Phase: Implementation Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script. Phase: Architecture and Design Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330). Note that this can be bypassed using XSS. Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation. Note that this can be bypassed using XSS. Use the ESAPI Session Management control. This control includes a component for CSRF. Do not use the GET method for any request that triggers a state change. Phase: Implementation Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### 4. [Medium] Missing Anti-clickjacking Header

- Срабатываний: 5
- CWE: 1021
- Пример: `http://dvwa/`
- Как исправить: Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app. If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

### 5. [Medium] Content Security Policy (CSP) Header Not Set

- Срабатываний: 4
- CWE: 693
- Пример: `http://dvwa/`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### 6. [Medium] CSP: Failure to Define Directive with No Fallback

- Срабатываний: 2
- CWE: 693
- Пример: `http://dvwa/vulnerabilities/csp/`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### 7. [Medium] CSP: Wildcard Directive

- Срабатываний: 2
- CWE: 693
- Пример: `http://dvwa/vulnerabilities/csp/`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### 8. [Medium] CSP: style-src unsafe-inline

- Срабатываний: 2
- CWE: 693
- Пример: `http://dvwa/vulnerabilities/csp/`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### 9. [Medium] Sub Resource Integrity Attribute Missing

- Срабатываний: 2
- CWE: 345
- Пример: `http://dvwa/vulnerabilities/captcha/`
- Как исправить: Provide a valid integrity attribute to the tag.

### 10. [Low] Information Disclosure - Debug Error Messages

- Срабатываний: 12
- CWE: 1295
- Пример: `http://dvwa/README.ar.md`
- Как исправить: Disable debugging messages before pushing to production.

### 11. [Low] Cookie No HttpOnly Flag

- Срабатываний: 5
- CWE: 1004
- Пример: `http://dvwa/`
- Как исправить: Ensure that the HttpOnly flag is set for all cookies.

### 12. [Low] Cookie without SameSite Attribute

- Срабатываний: 5
- CWE: 1275
- Пример: `http://dvwa/`
- Как исправить: Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.

### 13. [Low] Cross-Origin-Resource-Policy Header Missing or Invalid

- Срабатываний: 5
- CWE: 693
- Пример: `http://dvwa/robots.txt`
- Как исправить: Ensure that the application/web server sets the Cross-Origin-Resource-Policy header appropriately, and that it sets the Cross-Origin-Resource-Policy header to 'same-origin' for all web pages. 'same-site' is considered as less secured and should be avoided. If resources must be shared, set the header to 'cross-origin'. If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Resource-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-resource-policy).

### 14. [Low] In Page Banner Information Leak

- Срабатываний: 5
- CWE: 497
- Пример: `http://dvwa/compose.yml`
- Как исправить: Configure the server to prevent such information leaks. For example: Under Tomcat this is done via the "server" directive and implementation of custom error pages. Under Apache this is done via the "ServerSignature" and "ServerTokens" directives.

### 15. [Low] Permissions Policy Header Not Set

- Срабатываний: 5
- CWE: 693
- Пример: `http://dvwa/setup.php`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header.

### 16. [Low] Server Leaks Information via "X-Powered-By" HTTP Response Header Field(s)

- Срабатываний: 5
- CWE: 497
- Пример: `http://dvwa/`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is configured to suppress "X-Powered-By" headers.

### 17. [Low] Server Leaks Version Information via "Server" HTTP Response Header Field

- Срабатываний: 5
- CWE: 497
- Пример: `http://dvwa/robots.txt`
- Как исправить: Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### 18. [Low] Timestamp Disclosure - Unix

- Срабатываний: 5
- CWE: 497
- Пример: `http://dvwa/phpinfo.php`
- Как исправить: Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

### 19. [Low] X-Content-Type-Options Header Missing

- Срабатываний: 5
- CWE: 693
- Пример: `http://dvwa/`
- Как исправить: Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages. If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### 20. [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid

- Срабатываний: 4
- CWE: 693
- Пример: `http://dvwa/setup.php`
- Как исправить: Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents. If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

### 21. [Low] Cross-Origin-Opener-Policy Header Missing or Invalid

- Срабатываний: 4
- CWE: 693
- Пример: `http://dvwa/setup.php`
- Как исправить: Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents. 'same-origin-allow-popups' is considered as less secured and should be avoided. If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

### 22. [Low] Big Redirect Detected (Potential Sensitive Information Leak)

- Срабатываний: 2
- CWE: 201
- Пример: `http://dvwa/vulnerabilities`
- Как исправить: Ensure that no sensitive information is leaked via redirect responses. Redirect responses should have almost no content.

### 23. [Low] Cross-Domain JavaScript Source File Inclusion

- Срабатываний: 2
- CWE: 829
- Пример: `http://dvwa/vulnerabilities/captcha/`
- Как исправить: Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.

### 24. [Low] Private IP Disclosure

- Срабатываний: 2
- CWE: 497
- Пример: `http://dvwa/phpinfo.php`
- Как исправить: Remove the private IP address from the HTTP response body. For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.

### 25. [Low] Dangerous JS Functions

- Срабатываний: 1
- CWE: 749
- Пример: `http://dvwa/dvwa/js/dvwaPage.js`
- Как исправить: See the references for security advice on the use of these functions.

### 26. [Informational] Base64 Disclosure

- Срабатываний: 9
- CWE: 319
- Пример: `http://dvwa/README.fa.md`
- Как исправить: Manually confirm that the Base64 data does not leak sensitive information, and that the data cannot be aggregated/used to exploit other vulnerabilities.

### 27. [Informational] Modern Web Application

- Срабатываний: 5
- Пример: `http://dvwa/`
- Как исправить: This is an informational alert and so no changes are required.

### 28. [Informational] Sec-Fetch-Dest Header is Missing

- Срабатываний: 5
- CWE: 352
- Пример: `http://dvwa/sitemap.xml`
- Как исправить: Ensure that Sec-Fetch-Dest header is included in request headers.

### 29. [Informational] Sec-Fetch-Mode Header is Missing

- Срабатываний: 5
- CWE: 352
- Пример: `http://dvwa/sitemap.xml`
- Как исправить: Ensure that Sec-Fetch-Mode header is included in request headers.

### 30. [Informational] Sec-Fetch-Site Header is Missing

- Срабатываний: 5
- CWE: 352
- Пример: `http://dvwa/sitemap.xml`
- Как исправить: Ensure that Sec-Fetch-Site header is included in request headers.

### 31. [Informational] Sec-Fetch-User Header is Missing

- Срабатываний: 5
- CWE: 352
- Пример: `http://dvwa/sitemap.xml`
- Как исправить: Ensure that Sec-Fetch-User header is included in user initiated requests.

### 32. [Informational] Session Management Response Identified

- Срабатываний: 5
- Пример: `http://dvwa/`
- Как исправить: This is an informational alert rather than a vulnerability and so there is nothing to fix.

### 33. [Informational] Storable but Non-Cacheable Content

- Срабатываний: 5
- CWE: 524
- Пример: `http://dvwa/setup.php`
- Как исправить: нет рекомендации

### 34. [Informational] Information Disclosure - Sensitive Information in URL

- Срабатываний: 4
- CWE: 598
- Пример: `http://dvwa/vulnerabilities/brute/?Login=Login&password=ZAP&username=ZAP`
- Как исправить: Do not pass sensitive information in URIs.

### 35. [Informational] Storable and Cacheable Content

- Срабатываний: 4
- CWE: 524
- Пример: `http://dvwa/robots.txt`
- Как исправить: Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user: Cache-Control: no-cache, no-store, must-revalidate, private Pragma: no-cache Expires: 0 This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

### 36. [Informational] Information Disclosure - Suspicious Comments

- Срабатываний: 3
- CWE: 615
- Пример: `http://dvwa/setup.php`
- Как исправить: Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.

### 37. [Informational] Authentication Request Identified

- Срабатываний: 2
- Пример: `http://dvwa/vulnerabilities/brute/?Login=Login&password=ZAP&username=ZAP`
- Как исправить: This is an informational alert rather than a vulnerability and so there is nothing to fix.

### 38. [Informational] User Controllable HTML Element Attribute (Potential XSS)

- Срабатываний: 2
- CWE: 20
- Пример: `http://dvwa/instructions.php?doc=readme`
- Как исправить: Validate all input and sanitize output it before writing to any HTML attributes.

### 39. [Informational] Cookie Poisoning

- Срабатываний: 1
- CWE: 565
- Пример: `http://dvwa/security.php`
- Как исправить: Do not allow user input to control cookie names and values. If some query string parameters must be set in cookie values, be sure to filter out semicolon's that can serve as name/value pair delimiters.

### 40. [Informational] Non-Storable Content

- Срабатываний: 1
- CWE: 524
- Пример: `http://dvwa/vulnerabilities/`
- Как исправить: The content may be marked as storable by ensuring that the following conditions are satisfied: The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable) The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood) The "no-store" cache directive must not appear in the request or response header fields For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives) In addition to the conditions above, at least one of the following conditions must also be satisfied by the response: It must contain an "Expires" header field It must contain a "max-age" response directive For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive It must contain a "Cache Control Extension" that allows it to be cached It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).
