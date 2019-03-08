import re
from .name_that_color import NameThatColor

ntc = NameThatColor()


class ColorName:

    @staticmethod
    def get(hex_code):

        try:
            name = ntc.color_name(hex_code)
        except ValueError as e:
            return None

        name = name.replace(' ', '-')
        name = name.replace('/', '-')
        name = name.replace('\'', '')

        name = [s for s in name.split('-') if s]
        name = '-'.join(name)

        return name.lower()

    @classmethod
    def get_unique(cls, hex_code, color_dict):

        name = cls.get(hex_code)

        if name not in color_dict:
            return name

        is_match = cls.is_match(name)
        matches = [cn for cn in color_dict if is_match(cn)]

        return '{}-{}'.format(name, len(matches) + 1)

    @classmethod
    def is_match(cls, base_name):
        match_name_re = r'(?i)^(?:{0}-[0-9]+|{0})$'

        def result(name):

            name = cls.remove_suffix(name)
            match = re.match(
                match_name_re.format(name),
                base_name
            )

            return bool(match)

        return result

    @staticmethod
    def remove_suffix(name):
        name = name.split('-')

        if name[-1].isdigit():
            del name[-1]

        return '-'.join(name)
