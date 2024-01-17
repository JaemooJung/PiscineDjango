#!/usr/bin/python3

class Text(str):
    def __str__(self):
        return super().__str__()\
            .replace('<', '&lt;')\
                .replace('>', '&gt;')\
                    .replace('"', '&quot;')\
                        .replace('\n', '\n<br />\n')


class Elem:
    tag: str
    attr: dict
    content: list
    tag_type: str

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Error: unable to finish the operation.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if content is not None:
            self.add_content(content)
        if tag_type not in ['double', 'simple']:
            raise self.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        result = '<' + self.tag + self.__make_attr()
        if self.tag_type == 'double':
            result += '>' + self.__make_content() + '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            result += self.__make_content() + ' />'
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  ' + str(elem).replace('\n', '\n  ') + '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def test():
    img = Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    h1 = Elem('h1', content=Text('\"Oh no, not again!\"'))
    body = Elem('body', content=[h1, img])
    head = Elem('head', content=Elem('title', content=Text('\"Hello ground!\"')))
    html = Elem('html', content=[head, body])
    print(html)


if __name__ == '__main__':
    test()

