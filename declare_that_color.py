import sublime
import sublime_plugin
from .libs import Vanilla, Preprocessor

SETTINGS_FILE = 'declare_that_color.sublime-settings'


class DeclareThatColor(sublime_plugin.TextCommand):

    def __init__(self, view):

        self.view = view

        settings = sublime.load_settings(SETTINGS_FILE)
        css_selector = settings.get('css_selector', ':root')
        css_preprocessor = settings.get('css_preprocessor')

        if Preprocessor.is_supported(css_preprocessor):
            self.css = Preprocessor(css_preprocessor)
            return

        self.css = Vanilla(css_selector)

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        self.view.replace(
            edit, region, self.css.declare_hexcodes(buffer_))


class UndeclareThatColor(DeclareThatColor):

    def run(self, edit):

        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        self.view.replace(
            edit, region, self.css.undeclare_hexcodes(buffer_))
