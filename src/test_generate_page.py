import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_page(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title(" # Hello"), "Hello")
        self.assertEqual(extract_title("Hello\n# World"), "World")
        self.assertEqual(extract_title("   # Hello     "), "Hello")
