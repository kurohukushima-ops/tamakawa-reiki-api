from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("tamakawa_reiki_split.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "")
    results = []

    for item in data:
        if query in item["text"]:
            results.append(item)
            if len(results) >= 5:
                break

    return jsonify(results)

if __name__ == "__main__":
    app.run()
