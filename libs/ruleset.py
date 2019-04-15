import re

RULESET_RE = r'{}\s*?{{(?P<declarations>[\S\s]*?)}}\n{{0,3}}'


class RuleSet:

    def __init__(self, selector: str):

        self.selector = selector
        self.re = re.compile(
            RULESET_RE.format(self.selector),
            re.MULTILINE | re.IGNORECASE)

    def find_all(self, css):

        return tuple(m.group() for m in self.re.finditer(css))

    def remove_empty(self, css):

        for m in self.re.finditer(css):
            declarations = m.group('declarations')
            declarations_stripped = ''.join(declarations.split())

            if not declarations_stripped:
                css = css.replace(m.group(), '')

        return css

    def create(self, declarations: list):

        declarations = ['{}{}'.format('\t', d) for d in declarations]
        declarations_stringed = '\n'.join(declarations)

        return '{0} {{{2}{1}{2}}}{2}{2}'.format(
            self.selector, declarations_stringed, '\n')
