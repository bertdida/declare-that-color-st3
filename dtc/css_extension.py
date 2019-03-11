from .css import CSS
from .hex_code_declaration import HexCodeDeclaration
from .hex_code import HexCode
from .color_name import ColorName

PREFIX_DICT = {
    'stylus': '$',
    'sass': '$',
    'scss': '$',
    'less': '@'
}


class CSSExtension(CSS):

    error_422 = 'DeclareThatColor: css extension language not supported: {}'

    def __init__(self, language=None):

        if language is not self.is_supported(language):
            raise ValueError(error_422.format(language))

        separator = ' =' if language == 'stylus' else ':'

        self.prefix = PREFIX_DICT[language]

        self.hd = HexCodeDeclaration(self.prefix, separator)
        self.hc = HexCode()
        self.cn = ColorName()

    @staticmethod
    def is_supported(language):

        return language in PREFIX_DICT

    def get_variables_dict(self, css):

        return {n: self.hc.normalize(h)
                for n, h in self.hd.get_all(css) if self.hc.is_valid(h)}

    def remove_declarations(self, css):

        return self.hd.remove(css)

    @staticmethod
    def replace_variables_with_their_values(css, variables_dict):

        for var_name, hex_code in variables_dict.items():

            css = css.replace('{}'.format(var_name), hex_code)

        return css

    def set_variable(self, colors_dict):

        def variable(match):

            hex_code = self.hc.normalize(match.group())

            for name, _hex_code in colors_dict.items():
                if _hex_code == hex_code:
                    return '{}{}'.format(self.prefix, name)

        return variable

    @staticmethod
    def finalize_declarations(declarations):

        return '\n'.join(declarations) + ('\n' * 2)
