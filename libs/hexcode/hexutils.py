import re
import collections

HEX_CODE_RE = re.compile(r'(?i)#(?:[a-f0-9]{6}|[a-f0-9]{3})(?![a-z0-9])')

VALUE_ERROR_TEMPLATE = \
    "DeclareThatColor: invalid hexadecimal color value: {}"

IntegerRGB = collections.namedtuple('IntegerRGB', ['red', 'green', 'blue'])
IntegerHSL = \
    collections.namedtuple('IntegerHSL', ['hue', 'saturation', 'lightness'])


def is_valid(hex_code):

    return bool(HEX_CODE_RE.match(hex_code))


def find_all(string):

    return tuple(normalize(h)
                 for h in HEX_CODE_RE.findall(string) if is_valid(h))


def normalize(hex_code):

    if not is_valid(hex_code):
        raise ValueError(VALUE_ERROR_TEMPLATE.format(hex_code))

    hex_digits = hex_code.lstrip('#')

    if len(hex_digits) == 3:
        hex_digits = ''.join(2 * s for s in hex_digits)

    return '#{}'.format(hex_digits.lower())


def rgb(hex_code):

    hex_code = normalize(hex_code)
    hex_code = int(hex_code[1:], 16)

    return IntegerRGB(
        hex_code >> 16,
        hex_code >> 8 & 0xff,
        hex_code & 0xff
    )


def hsl(hex_code):

    r, g, b = rgb(hex_code)

    r /= 255
    g /= 255
    b /= 255

    max_ = max(r, max(g, b))
    min_ = min(r, min(g, b))

    delta = max_ - min_

    l = (max_ + min_) / 2

    s = 0
    if l > 0 and l < 1:
        s = delta / ((2 * l if l < 0.5 else 2 - 2 * l))

    h = 0
    if delta > 0:
        if max_ == r and max_ != g:
            h += (g - b) / delta

        if max_ == g and max_ != b:
            h += 2 + (b - r) / delta

        if max_ == b and max_ != r:
            h += 4 + (r - g) / delta

        h /= 6

    return IntegerHSL(
        round(h * 255),
        round(s * 255),
        round(l * 255)
    )
