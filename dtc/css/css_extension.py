from .css import CSS

PREFIX_DICT = {
    'sass': '$',
    'scss': '$',
    'less': '@'
}


class CSSExtension(CSS):

    def __init__(self, css, language=None):

        super(CSSExtension, self).__init__(css)

        if language not in PREFIX_DICT:
            language = 'sass'

        self.variable_prefix = PREFIX_DICT[language]

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

        return ['{}{}: {};'.format(self.variable_prefix, k, color_dict[k])
                for k in sorted(color_dict, key=self.alphanum)]

    def _format_declaration(self, declaration):

        return '{0}{1}{1}'.format(declaration, '\n')
