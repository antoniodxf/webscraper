from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(url):
    parsed = urlparse(url)
    full_url = (parsed.netloc + parsed.path).lower()
    return full_url.rstrip("/")


def get_heading_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    h1 = soup.find("h1")
    h2 = soup.find("h2")

    if h1 is not None:
        return h1.get_text()
    if h2 is not None:
        return h2.get_text()

    return ""

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    main = soup.find("main")
    paragraph = soup.find("p")

    if main is not None:
        main_p = main.find("p")
        if main_p is not None:
            return main_p.get_text()
    
    if paragraph is not None:
        return paragraph.get_text()
    
    if paragraph is None:
        return ""
    
    
    
    

       