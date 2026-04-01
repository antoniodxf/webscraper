import unittest
from crawl import normalize_url


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

if __name__ == "__main__":
    unittest.main()
