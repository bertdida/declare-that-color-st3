import re
from .hexcode import hexutils
from .hexcode import hexname
from .ruleset import RuleSet
from .declaration import Declaration


class Vanilla:

    prefix = '--'

    def __init__(self, selector=None):

        self.ruleset = RuleSet(selector)
        self.declaration = Declaration()

    def get(self, css):

        if not hexutils.get_all(css):
            return css

        varname_hex_map = self.get_varname_hex_map(css)

        css = self.remove_color_declarations(css)
        css = self.replace_varnames_with_hexcodes(css, varname_hex_map)

        colorname_hex_map = self.get_colorname_hex_map(css)

        set_variable_partial = self.set_variable(colorname_hex_map)
        css = hexutils.HEX_CODE_RE.sub(set_variable_partial, css)

        sorted_colornames = sorted(colorname_hex_map, key=self.natural_sort)
        declarations = [self.declaration.create(k, colorname_hex_map[k])
                        for k in sorted_colornames]

        return '{}{}'.format(self.format_declarations(declarations), css)

    def get_varname_hex_map(self, css):

        dict_ = {}

        for rule_set in self.get_rulesets(css):
            decs = self.declaration.get_all(rule_set)
            decs = tuple([n, hexutils.normalize(h)]
                         for n, h in decs if hexutils.is_valid(h))

            dict_.update({n: h for n, h in decs})

        return dict_

    def get_rulesets(self, css):

        return self.ruleset.get_all(css)

    def remove_color_declarations(self, css):

        for rule_set in self.get_rulesets(css):
            css = css.replace(rule_set, self.declaration.remove(rule_set))

        return self.ruleset.remove_empty(css)

    @staticmethod
    def replace_varnames_with_hexcodes(css, name_hex_map):

        for name, hex_code in name_hex_map.items():
            css = css.replace('var({})'.format(name), hex_code)

        return css

    def get_colorname_hex_map(self, css):

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

        for hex_code in hexutils.get_all(css):
            if hex_code not in hex_codes:
                hex_codes.append(hex_code)

        return tuple(hex_codes)

    def set_variable(self, colorname_hex_map):

        def variable(match):

            hex_code = hexutils.normalize(match.group())

            for name, _hex_code in colorname_hex_map.items():
                if _hex_code == hex_code:
                    return 'var({}{})'.format(self.prefix, name)

        return variable

    @staticmethod
    def natural_sort(string):

        return [int(s) if s.isdigit() else s.lower()
                for s in re.split(r'([0-9]+)', string)]

    def format_declarations(self, declarations):

        return self.ruleset.create(declarations)


PREPROCESSOR_PREFIX_MAP = {
    'stylus': '$',
    'sass': '$',
    'scss': '$',
    'less': '@'
}


class Preprocessor(Vanilla):

    def __init__(self, preprocessor=None):

        preprocessor = preprocessor if self.is_supported(
            preprocessor) else 'sass'
        separator = ' =' if preprocessor == 'stylus' else ':'

        self.prefix = PREPROCESSOR_PREFIX_MAP[preprocessor.lower()]
        self.declaration = Declaration(self.prefix, separator)

    @staticmethod
    def is_supported(preprocessor):

        if preprocessor is None:
            return False

        return preprocessor.lower() in PREPROCESSOR_PREFIX_MAP

    def get_varname_hex_map(self, css):

        return {n: hexutils.normalize(h)
                for n, h in self.declaration.get_all(css)
                if hexutils.is_valid(h)}

    def remove_color_declarations(self, css):

        return self.declaration.remove(css)

    @staticmethod
    def replace_varnames_with_hexcodes(css, name_hex_map):

        for name, hex_code in name_hex_map.items():
            name_re = r'{}{}'.format(re.escape(name), '(?![a-z0-9-:])')
            css = re.sub(name_re, hex_code, css)

        return css

    def set_variable(self, colors_dict):

        def variable(match):

            hex_code = hexutils.normalize(match.group())

            for name, _hex_code in colors_dict.items():
                if _hex_code == hex_code:
                    return '{}{}'.format(self.prefix, name)

        return variable

    @staticmethod
    def format_declarations(declarations):

        return '{0}{1}{1}{1}'.format('\n'.join(declarations), '\n')
