import requests
import json
import re
import time

BASE = "https://www.vill.tamakawa.fukushima.jp/reiki_int/reiki_honbun/c569RG"

def scrape_page(num):
    num_str = str(num).zfill(8)
    url = BASE + num_str + ".html"

    res = requests.get(url)

    if res.status_code != 200:
        return None

    res.encoding = "utf-8"
    text = res.text

    if "該当するデータがありません" in text:
        return None

    title_match = re.search(r"<title>(.*?)</title>", text)
    title = title_match.group(1) if title_match else "不明"

    clean_text = re.sub("<.*?>", "", text)

    return {
        "title": title,
        "url": url,
        "text": clean_text
    }

def main():
    results = []

    for i in range(1, 1000):  # とりあえず1000まで確認
        print("確認中:", i)
        data = scrape_page(i)

        if data:
            print("取得:", data["title"])
            results.append(data)

        time.sleep(0.3)

    with open("tamakawa_reiki_full.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("全文取得完了")

if __name__ == "__main__":
    main()
