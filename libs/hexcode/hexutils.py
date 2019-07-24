import re
import string

HEX_CODE_RE = re.compile(r'#(?:[a-f0-9]{6}|[a-f0-9]{3})(?![a-z0-9])',
                         re.IGNORECASE)

HEX_CODE_INVALID_MESG = \
    'DeclareThatColor: not a valid hexadecimal color value: {}'


def check_if_valid(func):
    def decorator(hex_code):
        if not is_valid(hex_code):
            raise ValueError(HEX_CODE_INVALID_MESG.format(hex_code))

        return func(hex_code)

    return decorator


def is_valid(hex_code):
    try:
        hex_digits = hex_code.lstrip('#')
    except AttributeError:
        return False

    has_only_hexdigits = all(c in string.hexdigits for c in hex_digits)
    is_length_allowed = len(hex_digits) in (3, 6)

    return has_only_hexdigits and is_length_allowed


def find_all(string):
    return tuple(h for h in HEX_CODE_RE.findall(string) if is_valid(h))


@check_if_valid
def normalize(hex_code):
    """Convert hex code to six digit lowercase notation.
    """
    hex_digits = hex_code.lstrip('#')

    if len(hex_digits) == 3:
        hex_digits = ''.join(2 * c for c in hex_digits)

    return '#{}'.format(hex_digits.lower())


def rgb(hex_code):
    hex_code = normalize(hex_code)
    hex_decimal = int(hex_code[1:], 16)

    return (
        hex_decimal >> 16,
        hex_decimal >> 8 & 0xff,
        hex_decimal & 0xff
    )


def hsl(hex_code):
    """This function does not return a correct HSL value.
    I intentionally didn't fix this to produce a similar
    result from the name that color tool.
    """
    r, g, b = rgb(hex_code)

    r /= 255
    g /= 255
    b /= 255

    max_ = max(r, max(g, b))
    min_ = min(r, min(g, b))

    delta = max_ - min_

    L = (max_ + min_) / 2

    s = 0
    if L > 0 and L < 1:
        s = delta / (2 * L if L < 0.5 else 2 - 2 * L)

    h = 0
    if delta > 0:
        if max_ == r and max_ != g:
            h += (g - b) / delta

        if max_ == g and max_ != b:
            h += 2 + (b - r) / delta

        if max_ == b and max_ != r:
            h += 4 + (r - g) / delta

        h /= 6

    return (
        int(h * 255),
        int(s * 255),
        int(L * 255)
    )
