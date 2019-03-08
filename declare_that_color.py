import sublime
import sublime_plugin
from .dtc import CSS
from .dtc import CSSExtension


class ColorDeclaration(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        buffer_ = self.view.substr(region)

        css_selector = ':root'
        css_extension = 'scss'

        if False:
            css = CSS(css=buffer_, selector=css_selector)
        else:
            css = CSSExtension(css=buffer_, language=css_extension)

        css.save_previous_declarations()
        css.remove_declarations()
        css.replace_variables_with_their_values()
        css.declare_variables()

        self.view.replace(edit, region, css.css)
