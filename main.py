import argparse
import os

from bs4 import BeautifulSoup
from selenium import webdriver

from utility import ext

url = 'https://ckarakoc.github.io' or 'https://www.codewars.com/kata/59e49b2afc3c494d5d00002a'
driver = None

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='The codewars url')
parser.add_argument('--driver', help='driver type (i.e. geckodriver (Firefox) | chromedriver (Chrome))', default='geckodriver')
args = parser.parse_args()
driver_type = args.driver

try:
	driver_type = driver_type if os.path.isfile(f'./drivers/{driver_type}.exe') else ''
	if driver_type == 'chromedriver':
		print('Chrome chosen.')
		options = webdriver.ChromeOptions()
		options.headless = True
		driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe', options=options)
	elif driver_type == 'geckodriver':
		print(f'Firefox chosen.')
		options = webdriver.FirefoxOptions()
		options.headless = True
		driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe', options=options)
	else:
		raise Exception('You should either download geckodriver or chromedriver and put in in the ./drivers folder.')

	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	kyu = 'kyu_7'
	ex = 'vowel_count'
	proglang = 'python'
	solution = 'sol'

	path = f'./kata/{proglang}/{kyu}/{ex}/'
	os.makedirs(os.path.dirname(path), exist_ok=True)

	with open(f'{path}{solution}{ext(proglang)[0]}', 'w') as out:
		out.write('Hello Solution2!')

	with open(f'{path}README.md', 'w') as out:
		out.write('Hello README2!')
finally:
	if driver is not None:
		driver.quit()

# noteworthy css classes: .CodeMirror-code