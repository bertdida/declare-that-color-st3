from .rule_set import RuleSet
from .hex_code_declaration import HexCodeDeclaration
from .hex_code import HexCode
from .color_name import ColorName


class CSS:

    prefix = '--'

    def __init__(self, selector=None):

        self.rs = RuleSet(selector)
        self.hd = HexCodeDeclaration()
        self.hc = HexCode()
        self.cn = ColorName()

    def get(self, css):

        variables_dict = self.get_variables_dict(css)

        css = self.remove_declarations(css)
        css = self.replace_variables_with_their_values(css, variables_dict)

        colors_dict = self.get_colors_dict(css)
        set_variable = self.set_variable(colors_dict)

        css = self.hc.regex.sub(set_variable, css)

        declarations = [self.hd.create(n, h) for n, h in colors_dict.items()]
        declarations = self.finalize_declarations(declarations)

        return declarations + css

    def get_variables_dict(self, css):

        variables_dict = {}

        for rule_set in self.rs.get_all(css):

            declarations = self.hd.get_all(rule_set)
            declarations = tuple([n, self.hc.normalize(h)]
                                 for n, h in declarations
                                 if self.hc.is_valid(h))

            variables_dict.update({n: h for n, h in declarations})

        return variables_dict

    def remove_declarations(self, css):

        for rule_set in self.rs.get_all(css):
            css = css.replace(rule_set, self.hd.remove(rule_set))

        return self.rs.remove_empty(css)

    @staticmethod
    def replace_variables_with_their_values(css, variables_dict):

        for var_name, hex_code in variables_dict.items():
            css = css.replace('var({})'.format(var_name), hex_code)

        return css

    def get_colors_dict(self, css):

        hex_codes = self.get_unique_hex_codes(css)
        colors_dict = {}

        for hex_code in hex_codes:

            name = self.cn.get(hex_code)

            if name is not None:
                name = self.cn.get_unique(hex_code, colors_dict)
                colors_dict[name] = hex_code

        return colors_dict

    def get_unique_hex_codes(self, css):

        hex_codes = self.hc.get_all(css)
        return tuple(dict.fromkeys(hex_codes))

    def set_variable(self, colors_dict):

        def variable(match):

            hex_code = self.hc.normalize(match.group())

            for name, _hex_code in colors_dict.items():
                if _hex_code == hex_code:
                    return 'var({}{})'.format(self.prefix, name)

        return variable

    def finalize_declarations(self, declarations):

        return self.rs.create(declarations)
