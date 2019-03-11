import re


class HexCodeDeclaration:

	regex = r'[ \t]*?(?P<prop_name>\{}[a-z0-9-]*?)\s*?{}\s*?' \
		r'(?P<hex_code>#(?:[a-f0-9]{{6}}|[a-f0-9]{{3}}));$\n{{0,3}}'

	prefix = '--'

	separator = ':'

	def __init__(self, prefix=None, separator=None):
		
		if prefix is not None:
			self.prefix = prefix


		if separator is not None:
			self.separator = separator


		self.regex = re.compile(
			self.regex.format(self.prefix, self.separator), re.MULTILINE | re.IGNORECASE)



	def get_all(self, css):

		return tuple([m.group('prop_name'),m.group('hex_code')]

			for m in self.regex.finditer(css))



	def remove(self, css):

		return self.regex.sub('', css)



	def create(self, prop_name, hex_code):
		
		return '{}{}{} {};'.format(
			self.prefix, prop_name, self.separator, hex_code)