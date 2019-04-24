import re
from .hexcode import hexutils, hexname
from .ruleset import RuleSet
from .hexdeclaration import HexDeclaration


class Vanilla:

    varname_prefix = '--'

    def __init__(self, selector: str = ':root', name_prefix: str = None):

        self.ruleset = RuleSet(selector)
        self.hexdeclaration = HexDeclaration()
        self.name_prefix = '' if name_prefix is None else name_prefix

    def declare_hexcodes(self, css):

        if not hexutils.find_all(css):
            return css

        css = self.undeclare_hexcodes(css)

        colorname_hex_map = self.get_colorname_hex_map(css)
        set_variable_name = self.set_variable_name(colorname_hex_map)

        css = hexutils.HEX_CODE_RE.sub(set_variable_name, css)
        declarations = self.get_declarations(colorname_hex_map)

        return '{}{}'.format(declarations, css)

    def undeclare_hexcodes(self, css):

        varname_hex_map = self.get_varname_hex_map(css)

        css = self.remove_hexcode_declarations(css)
        css = self.replace_varnames_with_hexcodes(css, varname_hex_map)

        return css

    def get_varname_hex_map(self, css):

        dict_ = {}
        _get_declarations = self.hexdeclaration.find_all

        for rule_set in self.get_rulesets(css):
            varname_hex = _get_declarations(rule_set)
            varname_hex = [(n, hexutils.normalize(h))
                           for n, h in varname_hex if hexutils.is_valid(h)]

            dict_.update({n: h for n, h in varname_hex})

        return dict_

    def get_rulesets(self, css):

        return self.ruleset.find_all(css)

    def remove_hexcode_declarations(self, css):

        remove_declarations = self.hexdeclaration.remove

        for rule_set in self.get_rulesets(css):
            css = css.replace(rule_set, remove_declarations(rule_set))

        return self.ruleset.remove_empty(css)

    @staticmethod
    def replace_varnames_with_hexcodes(css, varname_hex_map: dict):

        for name, hex_code in varname_hex_map.items():
            css = css.replace('var({})'.format(name), hex_code)

        return css

    def get_colorname_hex_map(self, css):

        dict_ = {}
        hex_codes = self.get_unique_hexcodes(css)

        for hex_code in hex_codes:
            name = hexname.get_unique(hex_code, dict_)
            dict_[name] = hex_code

        dict_ = \
            {'{}{}'.format(self.name_prefix, n): h for n, h in dict_.items()}

        return dict_

    @staticmethod
    def get_unique_hexcodes(css):

        hex_codes = []

        for hex_code in hexutils.find_all(css):
            hex_code = hexutils.normalize(hex_code)

            if hex_code not in hex_codes:
                hex_codes.append(hex_code)

        return tuple(hex_codes)

    def set_variable_name(self, colorname_hex_map: dict):

        def variable_name(match):

            match = match.group()

            if hexutils.is_valid(match):
                hex_code = hexutils.normalize(match)

                for name, _hex_code in colorname_hex_map.items():
                    if _hex_code == hex_code:
                        return self.format_variable_name(name)

            return match

        return variable_name

    def format_variable_name(self, color_name):

        return 'var({}{})'.format(self.varname_prefix, color_name)

    def get_declarations(self, colorname_hex_map: dict):

        create_declaration = self.hexdeclaration.create
        sorted_names = sorted(colorname_hex_map, key=self.natural_sort)

        declarations = [create_declaration(n, colorname_hex_map[n])
                        for n in sorted_names]

        return self.format_declarations(declarations)

    @staticmethod
    def natural_sort(string):

        return [int(s) if s.isdigit() else s.lower()
                for s in re.split(r'([0-9]+)', string)]

    def format_declarations(self, declarations: list):

        return self.ruleset.create(declarations)


PREPROCESSOR_PREFIX_MAP = {
    'stylus': '$',
    'sass': '$',
    'scss': '$',
    'less': '@'
}


class Preprocessor(Vanilla):

    def __init__(self, language: str, name_prefix: str = None):

        assignment_operator = ' = ' if language == 'stylus' else ': '
        statement_separator = '' if language == 'sass' else ';'

        self.varname_prefix = \
            PREPROCESSOR_PREFIX_MAP.get(language.lower(), '$')

        self.hexdeclaration = \
            HexDeclaration(self.varname_prefix,
                           assignment_operator,
                           statement_separator)

        self.name_prefix = '' if name_prefix is None else name_prefix

    @staticmethod
    def is_supported(language: str):

        try:
            return language.lower() in PREPROCESSOR_PREFIX_MAP
        except AttributeError:
            return False

    def get_varname_hex_map(self, css):

        return {n: hexutils.normalize(h)
                for n, h in self.hexdeclaration.find_all(css)
                if hexutils.is_valid(h)}

    def remove_hexcode_declarations(self, css):

        return self.hexdeclaration.remove(css)

    @staticmethod
    def replace_varnames_with_hexcodes(css, varname_hex_map: dict):

        for name, hex_code in varname_hex_map.items():
            name_re = r'{}{}'.format(re.escape(name), '(?![a-z0-9-:])')
            css = re.sub(name_re, hex_code, css)

        return css

    def format_variable_name(self, color_name):

        return '{}{}'.format(self.varname_prefix, color_name)

    @staticmethod
    def format_declarations(declarations: list):

        return '{0}{1}{1}'.format('\n'.join(declarations), '\n')
