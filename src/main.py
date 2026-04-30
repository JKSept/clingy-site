from textnode import TextNode, TextType


def main():
    new_node = TextNode("This is a test node", TextType.BOLD, "https://www.boot.dev")
    print(new_node)


main()

