from leafnode import LeafNode
from textnode import TextNode, TextType
from blocktype import BlockType
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


def split_nodes_image(old_nodes):
    new_nodes = []
    to_check = ""
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        matches = extract_markdown_images(old.text)

        if matches == []:
            new_nodes.append(old)
            continue
        
        to_check = old.text
        for match in matches:
            while True:
                sections = to_check.split(f"![{match[0]}]({match[1]})", 1)
                if len(sections) == 1:
                    break
                if not sections[0] == "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
                to_check = sections[1]

        if len(to_check) != 0:
            new_nodes.append(TextNode(to_check, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    to_check = ""
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        matches = extract_markdown_links(old.text)

        if matches == []:
            new_nodes.append(old)
            continue
        
        to_check = old.text
        for match in matches:
            while True:
                sections = to_check.split(f"[{match[0]}]({match[1]})", 1)
                if len(sections) == 1:
                    break
                if not sections[0] == "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
                to_check = sections[1]

    if len(to_check) != 0:
        new_nodes.append(TextNode(to_check, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    blocks = [block for block in blocks if block != "" and block != "\n"]
    return blocks

    
def block_to_blocktype(block):
    # Check if block is heading
    hash_found = False
    for ch in block[:7]:
        if ch == "#":
            hash_found = True
        elif ch == " ":
            if hash_found:
                return BlockType.HEADING
        else:
            break

    # Check if block is code
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Check it block is quote
    is_quote = True
    lines = block.split("\n")
    for line in lines:
        if not line.strip().startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    # Check if block is unordered list
    is_uList = True
    for line in lines:
        if not line.strip().startswith("- "):
            is_uList = False
            break
    if is_uList:
        return BlockType.UNORDERED_LIST

    # Check if block is ordered list
    number = 1
    is_uoList = True
    for line in lines:
        if not line.strip().startswith(f"{number}. "):
            is_uoList = False
            break
        number += 1
    if is_uoList:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

