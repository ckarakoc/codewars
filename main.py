import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# res = requests.get(url, timeout=(3.05, 27))
#
# soup = BeautifulSoup(res.content, 'html.parser')
# title_div = soup.find('div', {'class': 'bg-ui-section'})
#
# description = soup.find('div', {'id': 'description'})
# print(description)
# print(soup.select('h4'))

url = 'https://www.codewars.com/kata/59e49b2afc3c494d5d00002a'

options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
description = soup.find('div', {'id': 'description'})
with open('out.html', 'w') as f:
	f.write(str(description.prettify()))
