from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:]
    raise Exception("Given Markdown document does not contain a an h1 header.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""

    with open(from_path, "r") as file:
        markdown = file.read()

    template = ""

    with open(template_path, "r") as file:
        template = file.read()

    markdown_html = markdown_to_html_node(markdown).to_html()
    
    title = extract_title(markdown)
    print(f"Found title: {title}")
    
    template_replaced = template.replace("{{ Title }}", title)
    template_replaced = template_replaced.replace("{{ Content }}", markdown_html)
    
    if not os.path.exists(os.path.dirname(dest_path)):
        print(f"Dest path '{dest_path}' does not exist, creating it.")
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as file:
        file.write(template_replaced)






