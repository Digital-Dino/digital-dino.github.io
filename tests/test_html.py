import os
from html.parser import HTMLParser

class IndexParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_title = False
        self.has_meta = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.has_title = True
        if tag == 'meta':
            self.has_meta = True

def test_index_html_structure():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert '</a href>' not in content, "Invalid '</a href>' pattern found"

    parser = IndexParser()
    parser.feed(content)

    assert parser.has_title, "<title> tag not found"
    assert parser.has_meta, "<meta> tag not found"
