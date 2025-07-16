import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        cn1 = LeafNode("c1", "child1")
        cn2 = LeafNode("c2", "child2")
        pn = ParentNode("parent", [cn1, cn2])
        self.assertEqual(
            pn.to_html(),
            "<parent><c1>child1</c1><c2>child2</c2></parent>"
        )


if __name__ == "__main__":
    unittest.main()
