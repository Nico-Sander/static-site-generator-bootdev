from functions import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode

import unittest


class TestTextToHTMLNode(unittest.TestCase):
    def test_plain(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        node = TextNode("Link description", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link description")
        self.assertEqual(html_node.props, [{"href": "www.google.com"}])

    def test_image(self):
        node = TextNode("Image description", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, [
            {
                "src": "www.google.com",
                "alt": "Image description"
            }
        ])

    def test_invalid_text_type(self):
        node = TextNode("Invalid", "random")
        with self.assertRaises(Exception) as cm: # 'cm' is just a variable name for the context manager object
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Unknown TextType!")

    
