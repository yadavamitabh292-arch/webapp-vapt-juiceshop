# Web Application VAPT — OWASP Juice Shop

A Vulnerability Assessment and Penetration Testing (VAPT) project performed against **OWASP Juice Shop**, an intentionally vulnerable web application used for security training.

## Objective
Identify, exploit, and document common web application vulnerabilities (mapped to the OWASP Top 10) in a controlled, legal lab environment, and provide remediation guidance.

## Scope
- Target: OWASP Juice Shop — `http://127.0.0.1:3000` (local Docker lab instance)
- Type: Black-box Web Application Penetration Test
- Environment: Kali Linux, isolated Docker lab (no external exposure)

## Tools Used
- Nmap — service/port discovery
- Gobuster — content/directory discovery
- Burp Suite — traffic analysis, Repeater
- Hydra — brute-force testing

## Findings Summary

| # | Vulnerability | OWASP Category | Severity |
|---|---|---|---|
| 1 | SQL Injection (Login bypass) | A03:2021 – Injection | Critical |
| 2 | Reflected XSS (Search field) | A03:2021 – Injection | High |
| 3 | IDOR (Basket API) | A01:2021 – Broken Access Control | High |
| 4 | Sensitive Data Exposure (`/ftp`) | A05:2021 – Security Misconfiguration | Medium |
| 5 | Weak Password Policy / No Brute-Force Protection | A07:2021 – Auth Failures | Medium |

Full details, evidence screenshots, and remediation are in [`VAPT_Report.md`](./VAPT_Report.md).

## Repository Structure
```
webapp-vapt-juiceshop/
├── README.md              # This file
├── VAPT_Report.md          # Full VAPT report with findings & evidence
├── scripts/
│   └── sqli_login_bypass.py   # PoC script for Finding 1
└── screenshots/               # Evidence screenshots referenced in the report
```

## Disclaimer
All testing was performed against a **self-hosted, deliberately vulnerable application** (OWASP Juice Shop) in an isolated local lab, strictly for educational purposes. No real-world or third-party systems were targeted.

## Author
**Amitabh Yadav**
- LinkedIn: https://www.linkedin.com/in/amitabh-yadav-335150306/
- TryHackMe: https://tryhackme.com/p/yadavamitabh292
