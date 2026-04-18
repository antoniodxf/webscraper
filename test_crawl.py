import unittest
from crawl import normalize_url, get_heading_from_html, get_first_paragraph_from_html, get_urls_from_html, get_images_from_html


class TestCrawl(unittest.TestCase):
    def test_normalize_url_remove_https(self):
        input_url = "https://www.python.org/downloads/"
        actual = normalize_url(input_url)
        expected = "www.python.org/downloads"
        self.assertEqual(actual, expected)
    def test_normalize_url_remove_http(self):
        input_url = "http://www.python.org/downloads/"
        actual = normalize_url(input_url)
        expected = "www.python.org/downloads"
        self.assertEqual(actual, expected)
    def test_normalize_url_lowercase(self):
        input_url = "HTTPS://WWW.PYTHON.ORG/DOWNLOADS/"
        actual = normalize_url(input_url)
        expected = "www.python.org/downloads"
        self.assertEqual(actual, expected)
    def test_normalize_url_remove_trailing_slash(self):
        input_url = "https://www.python.org/downloads/"
        actual = normalize_url(input_url)
        expected = "www.python.org/downloads"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_returns_h1(self):
        input_body = '<html><body><h1>Test Title</h1></body></html>'
        actual = get_heading_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)
    def test_get_heading_from_html_h2_fallback(self):
        input_body = '<html><body><h2>Backup Title</h2></body></html>'
        actual = get_heading_from_html(input_body)
        expected = "Backup Title"
        self.assertEqual(actual, expected)
    def test_get_heading_from_html_no_heading(self):
        input_body = '<html><body><p>Not a heading</p></body></html>'
        actual = get_heading_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_only_first_p(self):
        input_body = '<html><body><p>First paragraph.</p><p>Second paragraph.</p></body></html>'
        actual = get_first_paragraph_from_html(input_body)
        expected = "First paragraph."
        self.assertEqual(actual, expected)
    def test_get_first_paragraph_from_html_no_p(self):
        input_body = '<html><body><h1>Test Title</h1></body></html>'
        actual = get_first_paragraph_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)
    def test_get_first_paragraph_from_html_p_in_main(self):
        input_body = '<html><body><main><p>Main paragraph.</p></main></body></html>'
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)
    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = """
        <html><body><p>Outside paragraph.</p>
            <main><p>Main paragraph.</p></main>
            </body></html>"""
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_absolute(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="https://other-page.com"><span>External</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://other-page.com"]
        self.assertEqual(actual, expected)
    def test_get_urls_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="/about"><span>About</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/about"]
        self.assertEqual(actual, expected)
    def test_get_urls_from_html_multiple(self):
        input_url = "https://crawler-test.com"
        input_body = """
        <html><body>
            <a href="/about"><span>About</span></a>
            <a href="https://other-page.com"><span>External</span></a>
            <a href="/contact"><span>Contact</span></a>
        </body></html>"""
        actual = get_urls_from_html(input_body, input_url)
        expected = [
        "https://crawler-test.com/about", 
        "https://other-page.com", 
        "https://crawler-test.com/contact"
        ]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]
        self.assertEqual(actual, expected)
    def test_get_images_from_html_external(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="https://other-page.com/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://other-page.com/logo.png"]
        self.assertEqual(actual, expected)
    def test_get_images_from_html_multiple(self):
        input_url = "https://crawler-test.com"
        input_body = """<html><body>
        <img src="https://crawler-test.com/logo.png" alt="Logo">
        <img src="/logo.png" alt="Logo">
        <img src="https://other-page.com/logo.png" alt="Logo">
    
        </body></html>"""
        actual = get_images_from_html(input_body, input_url)
        expected = [
        "https://crawler-test.com/logo.png",
        "https://crawler-test.com/logo.png",
        "https://other-page.com/logo.png"
        ]
        self.assertEqual(actual, expected)
    def test_get_images_from_html_ignores_img_without_src(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()

