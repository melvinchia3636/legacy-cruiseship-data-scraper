from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
import json

option = Options()
option.set_headless(True)

url = 'https://www.marinetraffic.com/en/data/?asset_type=vessels&columns=flag,shipname,photo,recognized_next_port,reported_eta,reported_destination,current_port,imo,ship_type,show_on_live_map,time_of_latest_position,lat_of_latest_position,lon_of_latest_position,notes&flag_in|in|Bahamas|flag_in=BS'
main_data = []
main_url = []
#options=option
driver = webdriver.Chrome()
'''
driver.get(url)
time.sleep(5)
for i in range(25):
	driver.find_element_by_tag_name('body').send_keys(Keys.END)
	url = [i.get_attribute('href') for i in driver.find_elements_by_class_name('ag-cell-content-link') if 'vessel' in i.get_attribute('href')]
	[main_url.append(i) for i in url]
	try: driver.find_element_by_xpath('//button[@title="Next page"]').click()
	except: pass
	print(url)

with open('url.dat', 'w') as writer:
	writer.write(','.join(main_url))
'''

url = open('url.dat', 'r').read().split(',')

for i in range(len(url)):
	driver.get(url[i])
	time.sleep(5)
	meta = driver.find_element_by_xpath('//script[@type="application/ld+json" and @data-react-helmet="true"]')
	main_data.append(eval(meta.get_attribute('innerHTML')))
	print(i)
	with open('data.json', 'w') as file:
		json.dump(main_data, file)
