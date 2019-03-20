import re

HEX_CODE_RE = re.compile(r'(?i)#(?:[a-f0-9]{6}|[a-f0-9]{3})(?![a-z0-9])')

HEX_CODE_INVALID_MESG = \
    'DeclareThatColor: not a valid hexadecimal color value: {}'


def check_if_valid(func):

    def decorator(hex_code):

        if not is_valid(hex_code):
            raise ValueError(HEX_CODE_INVALID_MESG.format(hex_code))

        return func(hex_code)

    return decorator


def is_valid(hex_code):

    return bool(HEX_CODE_RE.match(hex_code))


def find_all(string):

    return tuple(h for h in HEX_CODE_RE.findall(string) if is_valid(h))


@check_if_valid
def normalize(hex_code):

    hex_digits = hex_code.lstrip('#')

    if len(hex_digits) == 3:
        hex_digits = ''.join(2 * s for s in hex_digits)

    return '#{}'.format(hex_digits.lower())


def rgb(hex_code):

    hex_code = normalize(hex_code)
    hex_decimal = int(hex_code[1:], 16)

    return (
        hex_decimal >> 16,
        hex_decimal >> 8 & 0xff,
        hex_decimal & 0xff
    )


@check_if_valid
def hsl(hex_code):

    r, g, b = rgb(hex_code)

    r /= 255
    g /= 255
    b /= 255

    max_ = max(r, max(g, b))
    min_ = min(r, min(g, b))

    h = s = l = (max_ + min_) / 2

    if max_ == min_:
        h = s = 0
    else:

        d = max_ - min_
        s = d / (2 - max_ - min_) if l > 0.5 else d / (max_ + min_)

        if max_ == r:
            h = (g - b) / d + (6 if g < b else 0)

        if max_ == g:
            h = (b - r) / d + 2

        if max_ == b:
            h = (r - g) / d + 4

        h /= 6

    return (
        int(round(h * 360)),
        int(round(s * 100)),
        int(round(l * 100)),
    )
