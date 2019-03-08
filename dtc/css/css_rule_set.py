import re


class CSSRuleSet:

    regex = r'^{}\s*?{{(?P<declarations>[\S\s]*?)}}\n{{0,3}}'

    def __init__(self, block_selector):

        self.regex = re.compile(
            self.regex.format(block_selector), re.MULTILINE | re.IGNORECASE)

    def get_all(self, css):

        return tuple(m.group() for m in self.regex.finditer(css))

    def remove_empty(self, css):

        for m in self.regex.finditer(css):
            declarations = m.group('declarations')
            declarations = ''.join(declarations.split())

            if not declarations:
                css = css.replace(m.group(), '')

        return css
