import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("", TextType.PLAIN)
        node2 = TextNode("", TextType.PLAIN)
        self.assertEqual(node, node2)

    def test_n_eq(self):
        node = TextNode("Hello", TextType.PLAIN)
        node2 = TextNode("World", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_n_eq_2(self):
        node = TextNode("Hello", TextType.ITALIC)
        node2 = TextNode("Hello", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_n_eq_3(self):
        node = TextNode("Hello", TextType.PLAIN, "google.com")
        node2 = TextNode("Hello", TextType.PLAIN, "boot.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
