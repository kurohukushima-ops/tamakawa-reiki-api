import json
import re

with open("tamakawa_reiki_full.json", "r", encoding="utf-8") as f:
    data = json.load(f)

split_data = []

for ordinance in data:
    text = ordinance["text"]

    articles = re.split(r"(第[一二三四五六七八九十百千]+条)", text)

    for i in range(1, len(articles), 2):
        split_data.append({
            "title": ordinance["title"],
            "url": ordinance["url"],
            "article": articles[i],
            "text": articles[i+1].strip()
        })

with open("tamakawa_reiki_split.json", "w", encoding="utf-8") as f:
    json.dump(split_data, f, ensure_ascii=False, indent=2)

print("条単位JSON生成完了")
