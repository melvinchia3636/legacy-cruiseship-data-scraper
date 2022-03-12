from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml.html
import lxml.html.clean
import html
import threading
import logging
import json
import math
import re
import os


option = Options()
option.add_argument('--headless')
logging.basicConfig(level=logging.INFO)

def scrape_ship_company_url(datafilename):
	ori_url = 'https://www.cruisemapper.com/ships'
	driver = webdriver.Chrome(options=option)
	logging.info('WEBDRIVER OPENED')
	driver.get(ori_url)
	logging.info('WEBPAGE OPENED')
	url = [str([i.get_attribute('href'), int(i.find_element_by_class_name('badge').get_attribute('innerHTML'))]) for i in driver.find_element_by_class_name('asideList').find_elements_by_tag_name('a')]
	logging.info('DATA SUCCESSFULLY PARSED')
	driver.close()

	logging.info('DRIVER CLOSED')
	with open(datafilename+'.dat', 'w') as writer:
		writer.write('['+','.join(url)+']')
	logging.info('DATA SUCCESSFULLY DUMPED INTO cruise_company_url.dat')

def scrape_ship_name(url_data_file):
	urls = eval(open(url_data_file, 'r').read())

	def run(url, company):
		driver.get(url)
		href = [i.find_element_by_tag_name('a').get_attribute('href') for i in driver.find_elements_by_class_name('shipListItemContent')]
		with open(company+'.dat', 'a') as writer:
			writer.write(','.join(href)+',')

	driver = webdriver.Chrome()

	for i in urls:
		company=i[0].split('/')[-1]
		for j in range(1, math.ceil(i[1] / 15 )+1):
			run(i[0]+'?page='+str(j), company)
