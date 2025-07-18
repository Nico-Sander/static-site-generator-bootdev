from functions import split_nodes_delimiter
from textnode import TextNode, TextType

import unittest


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ])

    def test_split_italic_1(self):
        node = TextNode("This is text with a _italic block_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC)
            ])

    def test_split_bold_1(self):
        node = TextNode("**Bold** first word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Bold", TextType.BOLD),
                TextNode(" first word", TextType.TEXT)
            ]
        )

    def test_split_multi_code(self):
        node = TextNode("Here is the first `code block (1)` and here is the second `code block (2)`.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Here is the first ", TextType.TEXT),
                TextNode("code block (1)", TextType.CODE),
                TextNode(" and here is the second ", TextType.TEXT),
                TextNode("code block (2)", TextType.CODE),
                TextNode(".", TextType.TEXT)
            ]
        )

    def test_multi_nodes_bold_italic(self):
        node1 = TextNode("Node with _italic_ text", TextType.TEXT)
        node2 = TextNode("Node with **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Node with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
                TextNode("Node with **bold** text", TextType.TEXT)
            ]
        )
