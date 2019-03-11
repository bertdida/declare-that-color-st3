import re


class HexCode:

	regex = re.compile(r'(?i)#(?:[a-f0-9]{6}|[a-f0-9]{3})(?![a-z0-9])')

	@classmethod
	def get_all(cls, css):

		hex_codes = cls.regex.findall(css)
		hex_codes = tuple(
			cls.normalize(h) for h in hex_codes if cls.is_valid(h))

		return hex_codes

	@classmethod
	def is_valid(cls, hex_code):

		return bool(cls.regex.match(hex_code))

	@staticmethod
	def normalize(hex_code):

		hex_digits = hex_code.lstrip('#')

		if len(hex_digits) == 3:
			hex_digits = ''.join(2 * c for c in hex_digits)

		return '#' + hex_digits.lower()