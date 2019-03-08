import re


class CSSHexCodeVariables:

    regex = r'[ \t]*?(?P<name>\{}[a-z0-9-]*?)\s*?{}\s*?' \
        r'(?P<hex_code>#(?:[a-f0-9]{{6}}|[a-f0-9]{{3}}));$\n{{0,3}}'

    def __init__(self, variable_prefix, assignment_operator=None):

        if assignment_operator is None:
            assignment_operator = ':'

        self.regex = re.compile(
            self.regex.format(variable_prefix, assignment_operator.strip()),
            re.MULTILINE | re.IGNORECASE)

    def get_all(self, css):

        return {name: hex_code for name, hex_code in self.regex.findall(css)}

    def remove(self, css):

        return self.regex.sub('', css)
