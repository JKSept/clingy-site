import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node3 = TextNode("This is a text node", TextType.ITALIC_TEXT, "this is a url")
        node4 = TextNode("Hello world node", TextType.CODE_TEXT) 
        node5 = TextNode("testing", TextType.ALT_TEXT, "some url")
        self.assertEqual(node, node2, node3)


if __name__ == "__main__":
    unittest.main()
