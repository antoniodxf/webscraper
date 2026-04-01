from urllib.parse import urlparse

def normalize_url(url):
    parsed = urlparse(url)
    full_url = (parsed.netloc + parsed.path).lower()
    return full_url.rstrip("/")

print(normalize_url("HTTPS://WWW.PYTHON.ORG/DOWNLOADS/"))