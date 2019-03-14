import re

HEXCODE_DECLARATION_RE = (
    r'[ \t]*?(?P<prop_name>\{}[a-z0-9-]*?)\s*?{}\s*?'
    r'(?P<hex_code>#(?:[a-f0-9]{{6}}|[a-f0-9]{{3}}));$\n{{0,3}}'
)


class Declaration:

    prefix = '--'

    separator = ':'

    def __init__(self, prefix=None, separator=None):

        if prefix is not None:
            self.prefix = prefix

        if separator is not None:
            self.separator = separator

        self.re = re.compile(
            HEXCODE_DECLARATION_RE.format(self.prefix, self.separator),
            re.MULTILINE | re.IGNORECASE)

    def get_all(self, css):

        return [(m.group('prop_name'), m.group('hex_code'))
                for m in self.re.finditer(css)]

    def remove(self, css):

        return self.re.sub('', css)

    def create(self, prop_name, hex_code):

        return '{}{}{} {};'.format(
            self.prefix, prop_name, self.separator, hex_code)
