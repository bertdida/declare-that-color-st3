import sublime
import sublime_plugin
from .libs import css

SETTINGS_FILE = 'declare_that_color.sublime-settings'


def plugin_loaded():
    global css_obj
    settings = sublime.load_settings(SETTINGS_FILE)

    css_preprocessor = settings.get('css_preprocessor')
    css_selector = settings.get('css_selector')
    type_case = settings.get('type_case')

    if not css.Preprocessor.is_supported(css_preprocessor):
        css_preprocessor = None

    if not isinstance(css_selector, str):
        css_selector = ':root'

    if not isinstance(type_case, str) or css.is_supported_type_case(type_case):
        type_case = 'dash'

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
