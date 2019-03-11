import sublime
import sublime_plugin
from .dtc import CSS
from .dtc import CSSExtension

SETTINGS_FILE = 'declare_that_color.sublime-settings'


class DeclareThatColor(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

        settings = sublime.load_settings(SETTINGS_FILE)
        self.css_selector = settings.get('css_selector')
        self.css_extension = settings.get('css_extension')

        if CSSExtension.is_supported(self.css_extension):
            self.css = CSSExtension(self.css_extension)
        else:
            self.css = CSS(self.css_selector)


    def run(self, edit):
        region = sublime.Region(0, self.view.size())

        self.view.replace(
            edit, region, self.css.get(self.view.substr(region)))
