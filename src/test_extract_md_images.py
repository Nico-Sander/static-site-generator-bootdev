from functions import extract_markdown_images
import unittest

class TestExtractMDImages(unittest.TestCase):
    def test_extract_md_image_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches,
                         [
                            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                         ]
        )

    def test_extract_md_image_2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches,
                         [
                            ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
                         ])

