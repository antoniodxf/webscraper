import sys
from crawl import crawl_page


def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    base_url = sys.argv[1]
    print(f"starting crawl of: {base_url}")
    crawled_pages = crawl_page(base_url)
    print(f"Number of pages found: {len(crawled_pages)}")
    for page in crawled_pages.values():
        print(page)
    


    

if __name__ == "__main__":
    main()
