from blocktype import BlockType
from functions import block_to_blocktype
import unittest

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        md = "# Heading 1"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.HEADING)

    def test_heading_2(self):
        md = "## Heading 2"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.HEADING)

    def test_heading_3(self):
        md = "### Heading 3"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.HEADING)

    def test_heading_4(self):
        md = "#### Heading 4"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.HEADING)

    def test_heading_5(self):
        md = "##### Heading 5"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.HEADING)

    def test_heading_6(self):
        md = "###### Heading 6"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.HEADING)

    def test_heading_7(self):
        md = "####### Heading 7"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.PARAGRAPH)

    def test_None(self):
        md = "Hello"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.PARAGRAPH)

    def test_code(self):
        md = "```print(Hello World)```"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.CODE)

    def test_code_multiline(self):
        md = "```\nimport random\nprint(Hello World)\n```"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.CODE)

    def test_quote_true(self):
        md = "> Hello\n> World"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.QUOTE)

    def test_quote_false(self):
        md = "> Hello\nWorld"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.PARAGRAPH)

    def test_unordered_true(self):
        md = "- L1\n - L2"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.UNORDERED_LIST)

    def test_unordered_false(self):
        md = "- L1\nL2"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.PARAGRAPH)

    def test_ordered_true(self):
        md = "1. L1\n2. L2\n3. L3"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.ORDERED_LIST)

    def test_ordered_false_1(self):
        md = "L1 \n1. L2\n2. L3"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.PARAGRAPH)

    def test_ordered_false_2(self):
        md = "1. L1\n2. L2\n 4. L4"
        bt = block_to_blocktype(md)
        self.assertEqual(bt, BlockType.PARAGRAPH)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)
