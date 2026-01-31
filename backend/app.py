from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

PHISHING_SET = set()

# ---------- NORMALIZE FUNCTION ----------
def normalize_url(url: str) -> str:
    if not url:
        return ""

    url = url.strip().lower()

    # remove protocol
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]

    # remove www
    if url.startswith("www."):
        url = url[4:]

    # remove trailing slash
    url = url.rstrip("/")

    return url


# ---------- LOAD CSV SAFELY ----------
with open("phishing_site_urls.csv", encoding="utf-8", errors="ignore") as f:
    reader = csv.DictReader(f)

    for row in reader:
        raw_url = row.get("URL", "")

        if not raw_url:
            continue

        normalized = normalize_url(raw_url)

        # VERY IMPORTANT: empty values skip
        if normalized and "." in normalized:
            PHISHING_SET.add(normalized)

print("✅ Phishing URLs loaded:", len(PHISHING_SET))
print("🔍 Sample:", list(PHISHING_SET)[:5])


# ---------- API ----------
@app.route("/check", methods=["POST"])
def check_url():
    data = request.get_json()
    user_url = data.get("url", "")

    normalized_user_url = normalize_url(user_url)

    # 🔒 Exact match ONLY
    if normalized_user_url in PHISHING_SET:
        return jsonify({
            "status": "block",
            "reason": "URL found in phishing database"
        })

    return jsonify({
        "status": "allow",
        "reason": "URL is not found in phishing database"
    })


if __name__ == "__main__":
    app.run(debug=True)
