# A7 – Cryptography in Modern Networks (TLS Analysis)

## Overview
This project explores the use of cryptography in modern networks, with a focus on Transport Layer Security (TLS). The analysis is based on real-world observations using browser developer tools.

---

## TLS Analysis of Gmail

I analyzed the cryptographic implementation of Gmail using browser developer tools. The website uses HTTPS, indicating that TLS is enabled to secure communication between the client and server.

The connection is established using **TLS 1.3**, which provides strong encryption and forward secrecy. Additionally, Gmail enforces important security headers such as:

- **Strict-Transport-Security (HSTS)**
- **Content-Security-Policy (CSP)**

### Security Mechanisms

- **HSTS (Strict-Transport-Security)**  
  Ensures that all future connections are forced to use HTTPS, preventing downgrade attacks.

- **CSP (Content-Security-Policy)**  
  Restricts the execution of untrusted scripts, reducing the risk of Cross-Site Scripting (XSS) attacks.

---

## Key Insight

This analysis demonstrates that modern large-scale applications implement TLS alongside additional security mechanisms to provide a comprehensive and secure communication environment.

---


## Tools Used

- Google Chrome Developer Tools
- HTTPS / TLS inspection (Security & Network tab)

---

## Conclusion

TLS is a fundamental component of modern network security. However, its effectiveness is enhanced when combined with additional protections such as HSTS and CSP, as demonstrated in this analysis of Gmail.
