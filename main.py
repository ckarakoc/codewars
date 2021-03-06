from collections import Counter
import argparse, json, os, time, re

from bs4 import BeautifulSoup
from selenium import webdriver
from jinja2 import Environment, FileSystemLoader

from utility import ext, setup_logger, login, update_table_json
import config

if __name__ == '__main__':
	logger = setup_logger()
	driver = None

	parser = argparse.ArgumentParser()
	parser.add_argument('--url', help='The codewars url: https://www.codewars.com/kata/<some hash>/train/<some programming language>')
	parser.add_argument('--driver', help='driver type (i.e. geckodriver (Firefox) | chromedriver (Chrome))', default='geckodriver')
	parser.add_argument('--headless', action='store_true')
	args = parser.parse_args()
	driver_type = args.driver
	url = str(args.url)

	try:
		# Setup Selenium Driver
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

		# Setup Jinja2 Template Engine
		fileloader = FileSystemLoader('./assets/templates')
		env = Environment(loader=fileloader)

		# Get the pages
		login(driver)
		driver.get(url)
		time.sleep(3)

		soup = BeautifulSoup(driver.page_source, 'html.parser')

		soup_game_title = soup.find('div', {'class': 'game-title'})
		proglang = url.split('?')[0].rsplit('/')[-1].lower()
		kyu = '_'.join(re.sub('[^0-9a-zA-Z ]+', '', soup_game_title.find('div', {'class': 'small-hex'}).text.lower()).split()[::-1])
		ex = '_'.join(re.sub('[^0-9a-zA-Z ]+', '', soup_game_title.find('h4').text.lower()).split())

		title = soup_game_title.find('h4').text
		description = soup.find(id='description')
		description.attrs.clear()
		for hidden in description.find_all(style=re.compile(r'display:\s*none')):
			hidden.decompose()
		solution = soup.find('li', {'data-tab': 'solutions'}).find_all('pre', {'lang': proglang})[-1]
		solution.attrs.clear()

		path = f'kata/{proglang}/{kyu}/{ex}/'
		os.makedirs(os.path.dirname(path), exist_ok=True)

		# Make the HTML page
		_html = env.get_template('template.html').render(
			title=title,
			url=url,
			description=description,
			solution=solution
		)

		with open(f'{path}solution.html', 'w', encoding='utf-8') as out:
			out.write(str(_html))

		# Make the solution
		with open(f'{path}solution{ext(proglang)[0]}', 'w', encoding='utf-8') as out:
			out.write(str(solution.text))

		# Make the Markdown page
		_markdown = f'# [{title}]({url})\n## Description\n{description}\n<details><summary>Solution</summary>{solution.prettify()}</details>'
		with open(f'{path}README.md', 'w', encoding='utf-8') as out:
			out.write(str(_markdown))

		# Make the index.html page
		entry = {
			'title': str(title),
			'lang': str(proglang).capitalize(),
			'ext': str(ext(proglang)[0])[1:],
			'kyu': str(re.sub('[^0-9]+', '', kyu)),
			'solution': f'{getattr(config, "GITHUB_PAGES_URL")}/codewars/{path}solution.html',
			'repo': f'{getattr(config, "GITHUB_REPO_URL")}/codewars/tree/main/{path}',
			'kata': str(url)
		}

		update_table_json(entry)

		with open('assets/json/table.json') as table:
			table_data = json.load(table)

		stats = {
			'kata': len(table_data),
			'kyu': Counter(table_data[i]['kyu'] for i in range(len(table_data))),
			'lang': Counter(table_data[i]['lang'] for i in range(len(table_data)))
		}

		index_html = env.get_template('home.html').render(
			title=f'{getattr(config, "HOME_PAGE_TITLE")}',
			table=table_data,
			stats=stats,
		)

		with open(f'index.html', 'w', encoding='utf-8') as out:
			out.write(str(index_html))

	finally:
		if driver is not None:
			logger.info('Quiting driver')
			driver.quit()
		logger.info('Program exited')
