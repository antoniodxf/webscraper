from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests 


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

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    links = soup.find_all("a")
    urls = []

    for link in links:
        url = link.get("href")
        if url is not None:
            absolute_url = urljoin(base_url, url)
            urls.append(absolute_url) 
    
    return urls 

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    image_links = soup.find_all("img")

    image_urls = []

    for image in image_links:
        image_path = image.get("src")
        if image_path is not None:
            absolute_path = urljoin(base_url, image_path)
            image_urls.append(absolute_path)
    
    return image_urls 
    
def extract_page_data(html, page_url): 
    dictionary = {}    
    dictionary["url"] = page_url  
    dictionary["heading"] = get_heading_from_html(html)
    dictionary["first_paragraph"] = get_first_paragraph_from_html(html)
    dictionary["outgoing_links"] = get_urls_from_html(html, page_url)
    dictionary["image_urls"] = get_images_from_html(html, page_url)
    return dictionary  

def get_html(url):
    response = requests.get(url, headers={"User-Agent": "Bootcrawler/1.0"})
    if response.status_code >= 400:
        raise Exception(f"HTTP error: {response.status_code}")
    content_type = response.headers.get("Content-Type")
    if content_type is None or "text/html" not in content_type:
        raise Exception(f"Invalid content type: {content_type}")
    return response.text 
    
def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = base_url
    if page_data is None:
        page_data = {}
    parsed_base = urlparse(base_url)
    parsed_current = urlparse(current_url)
    if parsed_base.netloc != parsed_current.netloc:
        return
    normalized_url = normalize_url(current_url)
    if normalized_url in page_data:
        return
    html = get_html(current_url)

    page_data[normalized_url] = extract_page_data(html, current_url)
    urls = get_urls_from_html(html, current_url)
    for url in urls:
        crawl_page(base_url, url, page_data)
    return page_data
        


    

       