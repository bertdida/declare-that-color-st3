import sublime
import sublime_plugin
from .libs import Vanilla, Preprocessor

SETTINGS_FILE = 'declare_that_color.sublime-settings'


class DeclareThatColor(sublime_plugin.TextCommand):

    def __init__(self, view):

        self.view = view

        settings = sublime.load_settings(SETTINGS_FILE)
        self.css_selector = settings.get('css_selector')
        self.css_preprocessor = settings.get('css_preprocessor')

        if self.is_preprocessor_supported(self.css_preprocessor):
            self.css = Preprocessor(self.css_preprocessor)
        else:
            self.css = Vanilla(self.css_selector)

    @staticmethod
    def is_preprocessor_supported(preprocessor):

        return preprocessor is not None \
            and Preprocessor.is_supported(preprocessor)

    def run(self, edit):

        region, buffer_ = self.get_region_and_buffer()

        self.view.replace(
            edit, region, self.css.declare_hexcodes(buffer_))

    def get_region_and_buffer(self):

        region = sublime.Region(0, self.view.size())

        return (region, self.view.substr(region))


class UndeclareThatColor(DeclareThatColor):

    def run(self, edit):

        region, buffer_ = self.get_region_and_buffer()

        self.view.replace(
            edit, region, self.css.undeclare_hexcodes(buffer_))
