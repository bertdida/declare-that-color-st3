import re

HEXCODE_DECLARATION_RE = (
    r'[ \t]*?(?P<prop_name>\{}[a-z0-9-]*?)\s*?{}\s*?'
    r'(?P<hex_code>#(?:[a-f0-9]{{6}}|[a-f0-9]{{3}})){}$\n{{0,3}}'
)


class HexDeclaration:

    def __init__(self,
                 varname_prefix: str = '--',
                 assignment_operator: str = ':',
                 statement_separator: str = ';'):

        self.varname_prefix = varname_prefix
        self.assignment_operator = assignment_operator
        self.statement_separator = statement_separator

        self.re = re.compile(
            HEXCODE_DECLARATION_RE.format(
                self.varname_prefix,
                self.assignment_operator,
                self.statement_separator),
            re.MULTILINE | re.IGNORECASE)

    def find_all(self, css):

        return [(m.group('prop_name'), m.group('hex_code'))
                for m in self.re.finditer(css)]

    def remove(self, css):

        return self.re.sub('', css)

    def create(self, prop_name, hex_code):

        return '{}{}{}{}{}'.format(
            self.varname_prefix,
            prop_name,
            self.assignment_operator,
            hex_code,
            self.statement_separator)
