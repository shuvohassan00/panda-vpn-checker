import requests

def fetch_raw_combo(pastebin_url):
    raw_url = pastebin_url.replace("pastebin.com/", "pastebin.com/raw/")
    try:
        res = requests.get(raw_url)
        if res.status_code == 200:
            return res.text.splitlines()
    except:
        pass
    return []

def main():
    with open("links.txt", "r") as f:
        links = f.read().splitlines()

    combos = []
    for link in links:
        combos += fetch_raw_combo(link)

    with open("combo.txt", "w") as f:
        for combo in combos:
            f.write(combo + "\n")

    print(f"[+] Saved {len(combos)} combos.")

if __name__ == "__main__":
    main()
