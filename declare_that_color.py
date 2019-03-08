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

    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        file_content = self.view.substr(region)

        if False:
            css = CSS(css=file_content, selector=self.css_selector)
        else:
            css = CSSExtension(css=file_content, language=self.css_extension)

        css.save_previous_declarations()
        css.remove_declarations()
        css.replace_variables_with_their_values()
        css.declare_variables()

        self.view.replace(edit, region, css.css)
