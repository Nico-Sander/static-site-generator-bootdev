from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError

        if not self.tag:
            return self.value

        atts = super().props_to_html()

        return f'<{self.tag}{atts}>{self.value}</{self.tag}>'
