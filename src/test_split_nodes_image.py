import unittest

from textnode import TextNode, TextType
from functions import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_2_same_images(self):
        node = TextNode(
            "Image 1 ![image](www.google.com) is the same as Image 2 ![image](www.google.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Image 1 ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "www.google.com"),
                TextNode(" is the same as Image 2 ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "www.google.com"),
            ],
            new_nodes,
        )


    def test_split_nodes_images_multiple_nodes(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        node2 = TextNode(
            "![dog](dog.com) ![cat](cat.com)",
            TextType.TEXT
        )

        new_nodes = split_nodes_image([node1, node2])

        self.assertListEqual(
            [

                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("dog", TextType.IMAGE, "dog.com"),
                TextNode(" ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "cat.com")
            ],
            new_nodes
        )

    def test_no_image(self):
        node = TextNode("This is just simple text.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is just simple text.", TextType.TEXT)
            ],
            new_nodes
        )

    def test_text_after_image(self):
        node = TextNode("![image](image.com) <- This is an image.", TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "image.com"),
                TextNode(" <- This is an image.", TextType.TEXT)
            ],
            new_nodes
        )
