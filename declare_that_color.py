import sublime
import sublime_plugin
from .libs import css

SETTINGS_FILE = 'declare_that_color.sublime-settings'
DEFAULT_PREPROCESSOR = None
DEFAULT_SELECTOR = ':root'
DEFAULT_CASE = 'dash'

css_obj = None
settings = None


def plugin_loaded():

    global settings

    settings = sublime.load_settings(SETTINGS_FILE)
    instantiate_css_obj()

    settings.add_on_change('css_selector', instantiate_css_obj)


def instantiate_css_obj():

    global css_obj

    css_preprocessor = settings.get('css_preprocessor')
    css_selector = settings.get('css_selector')
    type_case = settings.get('type_case')

    if not css.Preprocessor.is_supported(css_preprocessor):
        css_preprocessor = DEFAULT_PREPROCESSOR

    if not isinstance(css_selector, str):
        css_selector = DEFAULT_SELECTOR

    if not all([isinstance(type_case, str),
                css.is_supported_type_case(type_case)]):
        type_case = DEFAULT_CASE

    settings.set('css_preprocessor', css_preprocessor)
    settings.set('css_selector', css_selector)
    settings.set('type_case', type_case)

    if settings.get('css_preprocessor') is not None:
        css_obj = css.Preprocessor(settings)
        return

    css_obj = css.Vanilla(settings)


class DeclareThatColor(sublime_plugin.TextCommand):

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        self.view.replace(edit, region, css_obj.declare_hexcodes(buffer_))


class UndeclareThatColor(sublime_plugin.TextCommand):

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        self.view.replace(edit, region, css_obj.undeclare_hexcodes(buffer_))
