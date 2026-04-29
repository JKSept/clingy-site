import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://example.com"}
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://example.com"'
        )

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://google.com",
                "target": "_blank"
            }
        )

        result = node.props_to_html()

        self.assertIn(' href="https://google.com"', result)
        self.assertIn(' target="_blank"', result)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")

        self.assertEqual(
            node.props_to_html(),
            ""
        )

    def test_repr(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            props={"class": "text"}
        )

        result = repr(node)

        self.assertIn("HTMLNode", result)
        self.assertIn("tag=p", result)


if __name__ == "__main__":
    unittest.main()
