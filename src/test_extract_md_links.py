from functions import extract_markdown_links
import unittest

class TestExtractMDLinks(unittest.TestCase):
    def test_extract_md_links_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches,
                         [
                            ("to boot dev", "https://www.boot.dev"),
                            ("to youtube", "https://www.youtube.com/@bootdotdev")
                         ])

    def test_extract_md_links_2(self):
        text = "This is a link [to google](www.google.com) and this is an image ![random image](www.randomimage.com)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches,
                         [
                            ("to google", "www.google.com")
                         ])
