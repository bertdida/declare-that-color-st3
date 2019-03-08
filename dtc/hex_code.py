import re

HEX_CODE_FINDER_RE = re.compile(
    r'(?i)#(?:[a-f0-9]{6}|[a-f0-9]{3})(?![a-z0-9])')

HEX_CODE_VALID_RE = re.compile(
    r'(?i)^#(?:[a-f0-9]{6}|[a-f0-9]{3})$')


class HexCode:

    @staticmethod
    def is_valid(hex_code):

        return bool(HEX_CODE_VALID_RE.match(hex_code))

    @classmethod
    def get_all(cls, string):

        hex_codes = HEX_CODE_FINDER_RE.findall(string)
        hex_codes = [cls.normalize(h) for h in hex_codes if cls.is_valid(hc)]

        # remove duplicates
        hex_codes = list(dict.fromkeys(hex_codes))

        return hex_codes

    @classmethod
    def normalize(cls, hex_code):

        if not cls.is_valid(hex_code):
            return hex_code

        hex_code = cls.to_six_digits(hex_code)
        hex_code = hex_code.lower()

        return hex_code

    @staticmethod
    def to_six_digits(hex_code):

        hex_digits = hex_code.lstrip('#')

        if len(hex_digits) == 3:
            hex_digits = ''.join(2 * c for c in hex_digits)

        return '#{}'.format(hex_digits)
