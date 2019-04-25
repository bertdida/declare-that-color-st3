import sublime
import sublime_plugin
from .libs import css

SETTINGS_FILE = 'declare_that_color.sublime-settings'
DEFAULT_PREPROCESSOR = None
DEFAULT_SELECTOR = ':root'
DEFAULT_CASE = 'dash'
DEFAULT_PREFIX = ''

libs_css = None
settings = None


def plugin_loaded():

    global settings

    settings = sublime.load_settings(SETTINGS_FILE)
    instantiate_libs_css()

    settings.add_on_change('css_selector', instantiate_libs_css)


def instantiate_libs_css():

    global libs_css

    css_preprocessor = settings.get('css_preprocessor')
    name_prefix = settings.get('color_name_prefix')
    css_selector = settings.get('css_selector')
    type_case = settings.get('type_case')

    if not css.Preprocessor.is_supported(css_preprocessor):
        css_preprocessor = DEFAULT_PREPROCESSOR

    if not isinstance(name_prefix, str):
        name_prefix = DEFAULT_PREFIX

    if not isinstance(css_selector, str):
        css_selector = DEFAULT_SELECTOR

    if not all([isinstance(type_case, str),
                css.is_supported_type_case(type_case)]):
        type_case = DEFAULT_CASE

    settings.set('css_preprocessor', css_preprocessor)
    settings.set('color_name_prefix', name_prefix)
    settings.set('css_selector', css_selector)
    settings.set('type_case', type_case)

    if settings.get('css_preprocessor') is not None:
        libs_css = css.Preprocessor(settings)
        return

    libs_css = css.Vanilla(settings)


class DeclareThatColor(sublime_plugin.TextCommand):

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        self.view.replace(edit, region, libs_css.declare_hexcodes(buffer_))


class UndeclareThatColor(sublime_plugin.TextCommand):

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        self.view.replace(edit, region, libs_css.undeclare_hexcodes(buffer_))
