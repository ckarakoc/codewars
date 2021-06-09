import argparse
import logging
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver

import config
from utility import ext, setup_logger, login

if __name__ == '__main__':
	logger = setup_logger()
	driver = None

	parser = argparse.ArgumentParser()
	parser.add_argument('--url', help='The codewars url', default='https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python')
	parser.add_argument('--driver', help='driver type (i.e. geckodriver (Firefox) | chromedriver (Chrome))', default='geckodriver')
	parser.add_argument('--headless', action='store_true')
	args = parser.parse_args()
	driver_type = args.driver
	url = args.url

	try:
		# Setup Driver
		driver_type = driver_type if os.path.isfile(f'./drivers/{driver_type}.exe') else ''
		if driver_type == 'chromedriver':
			logger.info('Chrome chosen')
			options = webdriver.ChromeOptions()
			options.headless = args.headless
			driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe', options=options)
		elif driver_type == 'geckodriver':
			logger.info('Firefox chosen')
			options = webdriver.FirefoxOptions()
			options.headless = args.headless
			driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe', options=options, service_log_path='./logs/geckodriver.log')
		else:
			logger.error(f'unknown driver_type: {driver_type}')
			raise Exception('You should either download geckodriver or chromedriver and put in in the ./drivers folder.')
		driver.set_page_load_timeout(30)

		login(driver)
		driver.get(url)

		time.sleep(3)

		# driver.find_element_by_xpath('//button[@type="submit"]').click()

		# driver.get(url)
		# soup = BeautifulSoup(driver.page_source, 'html.parser')

		kyu = 'kyu_7'
		ex = 'vowel_count'
		proglang = 'python'
		solution = 'sol'

		path = f'./kata/{proglang}/{kyu}/{ex}/'
		os.makedirs(os.path.dirname(path), exist_ok=True)

		# with open(f'{path}test.html', 'wb') as out:
		# 	out.write(soup.prettify(encoding='utf-8'))

		# with open(f'{path}{solution}{ext(proglang)[0]}', 'w') as out:
		# 	out.write(soup.contents)

		# with open(f'{path}README.md', 'w') as out:
		# 	out.write(str('READ'))
	finally:
		if driver is not None:
			logger.info('Quiting driver')
			driver.quit()
		logger.info('Program exited')
