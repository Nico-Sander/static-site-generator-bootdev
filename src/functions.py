from leafnode import LeafNode
from textnode import TextNode, TextType
import re

def text_node_to_html_node(text_node):
    text = text_node.text
    url = text_node.url

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text)

    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text, [{"href": url}])

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img",
            "",
            [{
                "src": url,
                "alt": text
            }]
        )

    else:
        raise Exception("Unknown TextType!")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        old_split = old.text.split(sep=delimiter)

        if len(old_split) % 2 == 0 and len(old_split) > 1:
            raise Exception(f"No closing delimiter ({delimiter}) found in '{old.text}'!")

        for i in range(len(old_split)):
            if old_split[i] != "":
                if i % 2 == 0:
                    tn = TextNode(old_split[i], TextType.TEXT)
                else:
                    tn = TextNode(old_split[i], text_type)
                new_nodes.append(tn)

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
