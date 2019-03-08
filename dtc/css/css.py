import re
from .css_hex_code_variable import CSSHexCodeVariables
from .css_rule_set import CSSRuleSet
from ..hex_code import HexCode, HEX_CODE_FINDER_RE
from ..colorname import ColorName


class CSS:

    declarations = {}

    variable_prefix = '--'

    block_selector = ':root'

    def __init__(self, css, block_selector=None):

        self.css = css

        if block_selector is not None:
            self.block_selector = block_selector

        self.hex_var = CSSHexCodeVariables(self.variable_prefix)
        self.rule_set = CSSRuleSet(self.block_selector)

        self.declaration_rule_sets = self.rule_set.get_all(self.css)

    def save_previous_declarations(self):

        for rule_set in self.declaration_rule_sets:
            self.declarations.update(self.hex_var.get_all(rule_set))

    def remove_declarations(self):

        for rule_set in self.declaration_rule_sets:
            self.css = self.css.replace(
                rule_set, self.hex_var.remove(rule_set))

        self.css = self.rule_set.remove_empty(self.css)

    def replace_variables_with_their_values(self):

        for var_name, hex_code in self.declarations.items():
            self.css = self.css.replace('var({})'.format(var_name), hex_code)

    def declare_variables(self):

        color_dict = self._get_color_dict()

        if not color_dict:
            return

        declaration = self._create_color_declaration(color_dict)

        set_variable = self._set_variable(color_dict)
        self.css = HEX_CODE_FINDER_RE.sub(set_variable, self.css)

        self.css = '{}{}'.format(declaration, self.css)

    def _get_color_dict(self):

        color_dict = {}

        for hex_code in HexCode.get_all(self.css):
            name = ColorName.get(hex_code)

            if name is not None:
                name = ColorName.get_unique(hex_code, color_dict)
                color_dict[name] = hex_code

        return color_dict

    def _set_variable(self, color_dict):

        def variable(match):

            hex_code = HexCode.normalize(match.group())

            for name, _hex_code in color_dict.items():
                if _hex_code == hex_code:
                    return self._format_variable(name)

        return variable

    def _format_variable(self, name):

        return 'var({}{})'.format(self.variable_prefix, name)

    def _create_color_declaration(self, color_dict):

        value_pairs = self._get_value_pairs(color_dict)
        declaration = '\n'.join(value_pairs)
        declaration = self._format_declaration(declaration)

        return declaration

    @staticmethod
    def alphanum(string):

        regex = re.compile(r'([0-9]+)')
        return [int(s) if s.isdigit() else s for s in regex.split(string)]

    def _get_value_pairs(self, color_dict):

        return ['\t{}{}: {};'.format(self.variable_prefix, k, color_dict[k])
                for k in sorted(color_dict, key=self.alphanum)]

    def _format_declaration(self, declaration):

        return '{0} {{{1}{2}{1} }}{1}{1}'.format(
            self.block_selector, '\n', declaration)
