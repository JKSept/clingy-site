from enum import Enum


class TextType(Enum):
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINK_TEXT = "anchor text"
    ALT_TEXT = "alt text"
    TEXT = "plain text"

class TextNode():
    def __init__(self, text, text_type, url=None):
        
        self.text = text
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        if (self.text == other.text 
            and self.text_type == other.text_type
            and self.url == other.url 
        ):
            return True
        return False 

    def __repr__(self):
        string = f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        return string
