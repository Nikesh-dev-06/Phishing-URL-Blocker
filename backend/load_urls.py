import pandas as pd

def load_phishing_urls():
    df = pd.read_csv("phishing_site_urls.csv")
    urls = set(df["URL"].astype(str).str.strip())
    return urls
