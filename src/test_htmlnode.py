import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        n = HTMLNode(
            "p",
            "Hello",
            None,
            {
                "href": "https://www.google.com",

                "target": "_blank"
            }
        )
        correct = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(n.props_to_html(), correct) 


    def test_props_to_html_1(self):
        n = HTMLNode(
            "p",
            "Hello",
            None,
            None
        )
        correct = ""
        self.assertEqual(n.props_to_html(), correct) 

    def test_props_to_html_2(self):
        n = HTMLNode(
            None,
            None,
            None,
            {
                "Hello": 1,

                "World": 2
            }
        )
        correct = ' Hello="1" World="2"'
        self.assertEqual(n.props_to_html(), correct) 


if __name__ == "__main__":
    unittest.main()
