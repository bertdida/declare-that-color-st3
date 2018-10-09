import re
from collections import OrderedDict
import sublime
import sublime_plugin
from .NameThatColor import NameThatColor


class DeclareThatColorCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        
        self.set_settings()
        self.ntc = NameThatColor()
        self.dict = OrderedDict()

        region = sublime.Region(0, self.view.size())
        contents = self.view.substr(region)

        new_contents = re.sub(r'#[0-9a-z]+', self.set_variable, contents, flags=re.I)
        new_contents = self.clean(new_contents) # Removes previous declarations
        new_contents = self.declarations(new_contents) + new_contents

        self.view.replace(edit, region, new_contents)

    def set_settings(self):
        settings = sublime.load_settings('DeclareThatColor.sublime-settings')
        self.prefix = self.get_prefix(settings)
        self.is_alphabetical = self.is_ordered_alphabetically(settings)
        self.is_vanilla = True if not self.prefix else False

    def get_prefix(self, settings):
        prefix = settings.get('variable_prefix', '')

        if prefix not in ['$', '@']:
            return ''
        return prefix

    def is_ordered_alphabetically(self, settings):
        result = settings.get('declare_alphabetically', False)

        if not type(result) == bool:
            return False
        return result

    def set_variable(self, match):
        code = match.group()
        code = code.lower()

        # Accepts only 3 or 6 digit valid hex codes
        if re.search(r'^#(?:[a-f0-9]{6}|[a-f0-9]{3})$', code) == None:
            return code

        # Makes sure, hex codes like #fff and #ffffff
        # are declared only once
        code = self.to_six_digit(code)

        name = self.ntc.name(code)
        name = name.replace(' ', '-')
        name = name.replace("'", '')

        if code in self.dict.values():
            name = self.get_name(code)
        elif name in self.dict:
            name = self.add_suffix(name)

        self.dict[name] = code
        return self.format(name)

    def to_six_digit(self, code):
        code = code.replace('#', '')

        if len(code) % 3 == 0:
            code = '#' + code
        if len(code) == 4:
            code = '#' + code[1:2] + code[1:2] + code[2:3] + code[2:3] + code[3:4] + code[3:4]
        return code

    def get_name(self, code):
        for key, val in self.dict.items():
            if val == code:
                return key

    def add_suffix(self, name):
        suffix = 1

        for item in self.dict.items():
            # The second condition avoids false positive items like;
            # name = silver
            # item[0] = silver-chalice
            # 
            # Where item[0] starts with silver, but not exactly what the program wants
            if item[0].startswith(name) and len(item[0]) < (len(name) + 2):
                suffix += 1
        return '{n}-{s}'.format(n=name, s=suffix)

    def format(self, name):
        if self.is_vanilla:
            return 'var(--{n})'.format(n=name)
        return self.prefix + name

    def clean(self, contents):
        for key, val in self.dict.items():
            regex = self.get_regex_cleaner(key)
            contents = re.sub(regex, '', contents, flags=re.I|re.M)

        if self.is_vanilla:
            contents = re.sub(r'^:root {\s*}$', '', contents, flags=re.M)

        contents = contents.lstrip('\n')
        return contents

    def get_regex_cleaner(self, var):
        regex = r'^\{p}{k}: \{p}{k};$'

        if self.is_vanilla:
            regex = r'^\s*--{k}: var\(--{k}\);$'
        return regex.format(p=self.prefix, k=var)

    def declarations(self, contents):
        dict_items = self.dict.items()
        value_pairs = []
        line = '\n'

        if self.is_alphabetical:
            dict_items = sorted(dict_items)

        for key, val in dict_items:
            # Doesn't include unused variable
            if self.format(key) not in contents:
                continue

            if self.is_vanilla:
                value_pairs.append('\t--{var}: {val};'.format(var=key, val=val))
            else:
                value_pairs.append('{var}: {val};'.format(var=self.format(key), val=val))

        dec = line.join(value_pairs)
        if self.is_vanilla:
            dec = ':root {{{l}{d}{l}}}'.format(l=line, d=dec)

        dec += line * 2
        return dec