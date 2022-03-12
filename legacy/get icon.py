import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from PIL import Image
import os

'''
ua = UserAgent()
headers = {'User-Agent': ua.random}
soup = BeautifulSoup(requests.get('https://www.cruisemapper.com/', headers=headers).content, 'lxml')
for name, url in [(i['alt'], i['src']) for i in soup.find('ul', {'class': 'mapFilterList'}).findAll('img')]:
	with open(name+'.png', 'wb') as file:
		file.write(requests.get(url, headers=headers).content)
'''

open('color.dat', 'w').write(str([(i.replace('.png', ''), Image.open('icon/'+i).getpixel((10, 12))) for i in os.listdir(os.getcwd()+r'\icon')]))