import re
from .hex_code_name import HexCodeName


class ColorName:

    regex = r'(?i)^(?:{0}-[0-9]+|{0})$'

    def __init__(self):
        self.hn = HexCodeName()

    def get(self, hex_code):

        try:
            return self.hn.color_name(hex_code)
        except ValueError as e:
            print(e)
            return None

    def get_unique(self, hex_code, color_dict):

        name = self.get(hex_code)

        if name not in color_dict:
            return name

        is_match = self.is_match(name)
        total_match = 1

        for n in color_dict:
            if is_match(n):
                total_match += 1

        return '{}-{}'.format(name, total_match)

    @classmethod
    def is_match(cls, base_name):

        def result(name):

            name = cls.remove_suffix(name)
            match = re.match(cls.regex.format(name), base_name)

            return bool(match)

        return result

    @staticmethod
    def remove_suffix(name):
        name = name.split('-')

        if name[-1].isdigit():
            del name[-1]

        return '-'.join(name)
