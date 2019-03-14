import sublime
import sublime_plugin
from .libs import Vanilla
from .libs import Preprocessor

SETTINGS_FILE = 'declare_that_color.sublime-settings'


class DeclareThatColor(sublime_plugin.TextCommand):

    def __init__(self, view):

        self.view = view

        settings = sublime.load_settings(SETTINGS_FILE)
        self.css_selector = settings.get('css_selector')
        self.css_preprocessor = settings.get('css_preprocessor')

        if Preprocessor.is_supported(self.css_preprocessor):
            self.css = Preprocessor(self.css_preprocessor)
        else:
            self.css = Vanilla(self.css_selector)

    def run(self, edit):

        region = sublime.Region(0, self.view.size())

        self.view.replace(
            edit, region, self.css.get(self.view.substr(region)))


class UndeclareThatColor(DeclareThatColor):

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        varname_hex_map = self.css.get_varname_hex_map(buffer_)

        buffer_ = self.css.remove_color_declarations(buffer_)
        buffer_ = self.css.replace_varnames_with_hexcodes(
            buffer_, varname_hex_map)

        self.view.replace(edit, region, buffer_)
