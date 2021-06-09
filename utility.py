import logging
import json
import time

import config
from errors import LoginError


def setup_logger(name='codewars', log_file='./logs/codewars.log', level=logging.DEBUG):
	"""Setup a logger."""
	formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d | %(levelname)s | %(module)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

	handler = logging.FileHandler(log_file)
	handler.setFormatter(formatter)

	logger = logging.getLogger(name)
	logger.setLevel(level)
	logger.addHandler(handler)

	return logger


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
			if str(extension['lang']).lower() == proglang.lower():
				return extension['extensions']
		return ['']


def log_and_raise_attr(logger_name, msg):
	logger = logging.getLogger(logger_name)
	logger.exception(msg)
	raise AttributeError(msg)


def login(driver):
	"""
	Logs in with your username/password from config.py on codewars.com
	:param driver: the selenium webdriver
	:return:
	"""
	driver.get('https://www.codewars.com/users/sign_in')

	user_email = driver.find_element_by_id('user_email')
	user_password = driver.find_element_by_id('user_password')

	user_email.send_keys(getattr(config, 'CW_USERNAME', lambda: log_and_raise_attr('codewars', 'CW_USERNAME in config.py')))
	user_password.send_keys(getattr(config, 'CW_PASSWORD', lambda: log_and_raise_attr('codewars', 'CW_PASSWORD in config.py')))
	user_password.submit()
	time.sleep(1)

	# Check if the email or password is correct
	if driver.find_element_by_id('flash').text:
		raise LoginError('Invalid email or password.')


def revert():
	# Revert the changes made if an error occurs by reading the log file
	pass
