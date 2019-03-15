import re
from .hexcode import hexutils
from .hexcode import hexname
from .ruleset import RuleSet
from .declaration import Declaration


class Vanilla:

    varname_prefix = '--'

    def __init__(self, selector: str = ':root'):

        self.ruleset = RuleSet(selector)
        self.declaration = Declaration()

    def declare_hexcodes(self, css):

        if not hexutils.find_all(css):
            return css

        css = self.undeclare_hexcodes(css)

        name_hex_pairs = self.get_colorname_hex_pairs(css)
        set_variable = self.set_variable_names(name_hex_pairs)

        css = hexutils.HEX_CODE_RE.sub(set_variable, css)
        declarations = self.get_declarations(name_hex_pairs)

        return '{}{}'.format(declarations, css)

    def undeclare_hexcodes(self, css):

        name_hex_pairs = self.get_varname_hex_pairs(css)

        css = self.remove_hexcode_declarations(css)
        css = self.replace_varnames_with_hexcodes(css, name_hex_pairs)

        return css

    def get_varname_hex_pairs(self, css):

        dict_ = {}
        _get_declarations = self.declaration.find_all

        for rule_set in self.get_rulesets(css):
            varname_hex = _get_declarations(rule_set)
            varname_hex = [(n, hexutils.normalize(h))
                           for n, h in varname_hex if hexutils.is_valid(h)]

            dict_.update({n: h for n, h in varname_hex})

        return dict_

    def get_rulesets(self, css):

        return self.ruleset.find_all(css)

    def remove_hexcode_declarations(self, css):

        remove_declarations = self.declaration.remove

        for rule_set in self.get_rulesets(css):
            css = css.replace(rule_set, remove_declarations(rule_set))

        return self.ruleset.remove_empty(css)

    @staticmethod
    def replace_varnames_with_hexcodes(css, name_hex_pairs: dict):

        for name, hex_code in name_hex_pairs.items():
            css = css.replace('var({})'.format(name), hex_code)

        return css

    def get_colorname_hex_pairs(self, css):

        hex_codes = self.get_unique_hexcodes(css)
        dict_ = {}

        for hex_code in hex_codes:
            name = hexname.get(hex_code)

            if name is not None:
                name = hexname.get_unique(hex_code, dict_)
                dict_[name] = hex_code

        return dict_

    @staticmethod
    def get_unique_hexcodes(css):

        hex_codes = []

        for hex_code in hexutils.find_all(css):
            if hex_code not in hex_codes:
                hex_codes.append(hex_code)

        return tuple(hex_codes)

    def set_variable_names(self, name_hex_pairs: dict):

        def variable_name(match):

            hex_code = hexutils.normalize(match.group())

            for name, _hex_code in name_hex_pairs.items():
                if _hex_code == hex_code:
                    return self.format_variable_name(name)

            return hex_code

        return variable_name

    def format_variable_name(self, name):

        return 'var({}{})'.format(self.varname_prefix, name)

    def get_declarations(self, name_hex_pairs: dict):

        create_declaration = self.declaration.create
        sorted_names = sorted(name_hex_pairs, key=self.natural_sort)

        declarations = [create_declaration(n, name_hex_pairs[n])
                        for n in sorted_names]

        return self.format_declarations(declarations)

    @staticmethod
    def natural_sort(string):

        return [int(s) if s.isdigit() else s.lower()
                for s in re.split(r'([0-9]+)', string)]

    def format_declarations(self, declarations: list):

        return self.ruleset.create(declarations)


PREPROCESSOR_PREFIX_PAIRS = {
    'stylus': '$',
    'sass': '$',
    'scss': '$',
    'less': '@'
}


class Preprocessor(Vanilla):

    def __init__(self, preprocessor: str):

        assignment_operator = ' =' if preprocessor == 'stylus' else ':'
        statement_separator = '' if preprocessor == 'sass' else ';'

        self.varname_prefix = \
            PREPROCESSOR_PREFIX_PAIRS.get(preprocessor.lower(), '$')

        self.declaration = \
            Declaration(self.varname_prefix,
                        assignment_operator,
                        statement_separator)

    @staticmethod
    def is_supported(preprocessor):

        try:
            return preprocessor.lower() in PREPROCESSOR_PREFIX_PAIRS
        except AttributeError:
            return False

    def get_varname_hex_pairs(self, css):

        return {n: hexutils.normalize(h)
                for n, h in self.declaration.find_all(css)
                if hexutils.is_valid(h)}

    def remove_hexcode_declarations(self, css):

        return self.declaration.remove(css)

    @staticmethod
    def replace_varnames_with_hexcodes(css, name_hex_pairs: dict):

        for name, hex_code in name_hex_pairs.items():
            name_re = r'{}{}'.format(re.escape(name), '(?![a-z0-9-:])')
            css = re.sub(name_re, hex_code, css)

        return css

    def format_variable_name(self, name):

        return '{}{}'.format(self.varname_prefix, name)

    @staticmethod
    def format_declarations(declarations: list):

        return '{0}{1}{1}'.format('\n'.join(declarations), '\n')
