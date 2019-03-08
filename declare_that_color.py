import sublime
import sublime_plugin
from .dtc import CSS
from .dtc import CSSExtension


class DeclareThatColor(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        file_content = self.view.substr(region)

        css_selector = ':root'
        css_extension = 'scss'

        if False:
            css = CSS(css=file_content, selector=css_selector)
        else:
            css = CSSExtension(css=file_content, language=css_extension)

        css.save_previous_declarations()
        css.remove_declarations()
        css.replace_variables_with_their_values()
        css.declare_variables()

        self.view.replace(edit, region, css.css)
