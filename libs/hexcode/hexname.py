import os
import re
import sublime
from . import hexutils

MATCH_NAME_RE = r'^(?:{0}-[0-9]+|{0})$'
LOAD_DATA_DELAY = 1000  # milliseconds

package_path = os.path.join(*__package__.split('.'))
color_data_path = os.path.join('Packages', package_path, 'data.json')
color_data = None


def _load_color_data():
    global color_data

    color_data_file = sublime.load_resource(color_data_path)
    color_data = sublime.decode_value(color_data_file)


# Fix for IOError("resource not found")
sublime.set_timeout(_load_color_data, LOAD_DATA_DELAY)


def get(hex_code):
    hex_code = hexutils.normalize(hex_code)
    r, g, b = hexutils.rgb(hex_code)
    h, s, L = hexutils.hsl(hex_code)

    color_name = None
    min_diff = None

    for name, color in color_data.items():
        if hex_code == color['hex']:
            return name

        _r, _g, _b = color['rgb']
        _h, _s, _L = color['hsl']

        rgb_diff = (
            pow(r - _r, 2) +
            pow(g - _g, 2) +
            pow(b - _b, 2)
        )

        hsl_diff = (
            pow(h - _h, 2) +
            pow(s - _s, 2) +
            pow(L - _L, 2)
        )

        diff = rgb_diff + hsl_diff * 2

        if min_diff is None or min_diff > diff:
            min_diff = diff
            color_name = name

    return color_name


def get_unique(hex_code, names: list):
    current_name = get(hex_code)

    if current_name not in names:
        return current_name

    _is_match = is_match(current_name)
    matches = [n for n in names if _is_match(n)]

    return '{}-{}'.format(current_name, len(matches) + 1)


def is_match(base_name):
    def result(name):
        name = strip_num_suffix(name)
        match = re.match(MATCH_NAME_RE.format(name), base_name, re.IGNORECASE)

        return bool(match)

    return result


def strip_num_suffix(name):
    *rest, last = name.split('-')

    if not last.isdigit():
        return name

    return '-'.join(rest)
