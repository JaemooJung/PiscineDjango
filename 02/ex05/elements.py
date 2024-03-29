#!/usr/bin/env python3
from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', attr=attr, content=content)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='simple')

def test1():
    print(Html([Head(), Body()]))

def test2():
    h1 = H1(Text('Oh no, not again!'))
    img = Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
    body = Body([h1, img])
    head = Head(Title(Text('Hello ground!')))
    html = Html([head, body])
    print(html)

if __name__ == '__main__':
    print("--test1--")
    test1()
    print("--test2--")
    test2()