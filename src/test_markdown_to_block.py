import unittest
from functions import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        ) 

    def test_md_to_blocks_blanklines(self):
        md = """
This is **bolded** paragraph


This is another paragraph after an extra blankline
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph after an extra blankline\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"
            ]
        )


    def test_md_to_blocks_leading_whitespace(self):
        md = """
This is a paragraph

   This is another paragraph with 3 leading spaces
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph with 3 leading spaces"
            ]
        )

