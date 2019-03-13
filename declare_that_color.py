import sublime
import sublime_plugin
from .dtc import Vanilla
from .dtc import Preprocessor

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
