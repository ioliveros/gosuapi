import requests
import time
from bs4 import BeautifulSoup

def web_bsoupify(url=None,src_code=None,soup_txt=None):
	if not url: return('No url found')
	def call_request(url):
		try:
			src_code = requests.get(url).text
			soup_txt = BeautifulSoup(src_code)
			return soup_txt
		except Exception as err:
			print('Error request: {0}, retrying.. '.format(err))
			time.sleep(1)	
			return call_request(url)
	return call_request(url)
