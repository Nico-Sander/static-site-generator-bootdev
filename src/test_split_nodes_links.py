import unittest

from textnode import TextType, TextNode
from functions import split_nodes_link

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes
        )

    def test_split_nodes_2_same_links(self):
        node = TextNode("Link 1 [link](link) Link 2 [link](link)", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Link 1 ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link"),
                TextNode(" Link 2 ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link")
            ],
            new_nodes
        )

    def test_text_after_link(self):
        node = TextNode("[link](link) and text", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "link"),
                TextNode(" and text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_multiple_nodes(self):
        node1 = TextNode("Text with link [link](link) and another [link2](link2)", TextType.TEXT)
        node2 = TextNode("New text with link [link3](link3) and an image ![image](image)", TextType.TEXT)

        new_nodes = split_nodes_link([node1, node2])

        self.assertListEqual(
            [
                TextNode("Text with link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "link2"),
                TextNode("New text with link ", TextType.TEXT),
                TextNode("link3", TextType.LINK, "link3"),
                TextNode(" and an image ![image](image)", TextType.TEXT)
            ],
            new_nodes
        )
