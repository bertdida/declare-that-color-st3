from .css import CSS
from .css_hex_code_variable import CSSHexCodeVariables

PREFIX_DICT = {
    'stylus': '$',
    'sass': '$',
    'scss': '$',
    'less': '@'
}


class CSSExtension(CSS):

    assignment_operator = ':'

    def __init__(self, css, language=None):

        self.css = css

        language = 'sass' if not self.is_supported(language) else language
        self.variable_prefix = PREFIX_DICT[language]

        if language == 'stylus':
            self.assignment_operator = ' ='

        self.hex_var = CSSHexCodeVariables(
            self.variable_prefix, self.assignment_operator)

    @staticmethod
    def is_supported(language):

        return language in PREFIX_DICT

    def save_previous_declarations(self):

        self.declarations = self.hex_var.get_all(self.css)

    def remove_declarations(self):

        self.css = self.hex_var.remove(self.css)

    def replace_variables_with_their_values(self):

        for var_name, hex_code in self.declarations.items():
            self.css = self.css.replace('{}'.format(var_name), hex_code)

    def _format_variable(self, name):

        return '{}{}'.format(self.variable_prefix, name)

    def _get_value_pairs(self, color_dict):

        return ['{}{}{} {};'.format(
            self.variable_prefix, k, self.assignment_operator, color_dict[k])
            for k in sorted(color_dict, key=self.alphanum)]

    @staticmethod
    def _format_declaration(declaration):

        return '{0}{1}{1}'.format(declaration, '\n')
