import requests
from bs4 import BeautifulSoup

def get_pastebin_links(query):
    url = f"https://www.google.com/search?q=site:pastebin.com+{query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if "pastebin.com" in href and "/raw/" not in href:
            link = href.split("&")[0].replace("/url?q=", "")
            links.append(link)

    return links

if __name__ == "__main__":
    query = "'email:pass' vpn"
    links = get_pastebin_links(query)
    with open("links.txt", "w") as f:
        for link in links:
            f.write(link + "\n")
    print(f"[+] Found {len(links)} links.")
