import csv

with open("phishing_site_urls.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("CSV HEADERS:", reader.fieldnames)

    for i, row in enumerate(reader):
        print(row)
        if i == 5:
            break
