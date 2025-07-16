from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        self.value = None

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode dose not have a tag. This is not possible.")

        if not self.children:
            raise ValueError("ParentNode does not have any children. This is not possible.")


        child_str = ""
        for child in self.children:
            child_str += child.to_html()

        return f"<{self.tag}>{child_str}</{self.tag}>"
