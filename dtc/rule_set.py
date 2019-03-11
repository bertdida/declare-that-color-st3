import re


class RuleSet:

    regex = r'{}\s*?{{(?P<declarations>[\S\s]*?)}}\n{{0,3}}'

    selector = ':root'

    def __init__(self, selector=None):

        if selector is not None:
            self.selector = selector

        self.regex = re.compile(
            self.regex.format(self.selector), re.MULTILINE | re.IGNORECASE)

    def get_all(self, css):
        return tuple(m.group() for m in self.regex.finditer(css))

    def remove_empty(self, css):

        for m in self.regex.finditer(css):
            dec = m.group('declarations')
            dec = ''.join(dec.split())

            if not dec:
                css = css.replace(m.group(), '')

        return css

    def create(self, declarations):

        declarations = ['\t' + d for d in declarations]
        declarations = '\n'.join(declarations)

        return '{0} {{{1}{2}{1}}}{1}{1}'.format(
            self.selector, '\n', declarations)
