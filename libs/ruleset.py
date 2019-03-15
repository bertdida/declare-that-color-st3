import re

RULESET_RE = r'{}\s*?{{(?P<declarations>[\S\s]*?)}}\n{{0,3}}'


class RuleSet:

    def __init__(self, selector):

        self.selector = selector
        self.re = re.compile(
            RULESET_RE.format(self.selector), re.MULTILINE | re.IGNORECASE)

    def get_all(self, css):

        return tuple(m.group() for m in self.re.finditer(css))

    def remove_empty(self, css):

        for m in self.re.finditer(css):
            decs = m.group('declarations')
            decs = ''.join(decs.split())

            if not decs:
                css = css.replace(m.group(), '')

        return css

    def create(self, declarations):

        declarations = ['{}{}'.format('\t', d) for d in declarations]
        declarations = '\n'.join(declarations)

        return '{0} {{{2}{1}{2}}}{2}{2}'.format(
            self.selector, declarations, '\n')
