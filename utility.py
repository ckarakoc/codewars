import json


def ext(proglang='text', file='extensions.json'):
	"""
	Returns an array of extensions used for the `proglang`.
	:param proglang: The programming language
	:param file: a modified json of https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41
	:return: an array of extensions.
	"""
	with open(file) as extensions:
		data = json.load(extensions)
		for extension in data:
			if str(extension['name']).lower() == proglang.lower():
				return extension['extensions']
		return ['']


def revert():
	# Revert the changes made if an error occurs by reading the log file
	pass
