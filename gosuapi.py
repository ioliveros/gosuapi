import re
from utils import *

"""
	GosuGamers Web API Crawler for dota2 ver. 1.a
	gosugamers.net/dota2 
	custom WebAPI crawler
	Author: ioliveros

"""

def headlines(url='http://www.gosugamers.net/dota2'):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'
	
	for div in soup_text.findAll('div'):
		if div.attrs.get('class'):
			if 'showcase-content' in div.attrs['class']:
				row = {}
				for obj in div.findAll('a'):
					row["href"] = url.strip('/dota2/')+obj.get('href')
				for obj in div.findAll('img'):
					row["desc"] = obj.get('alt')
					row["img"] = url.strip('/dota2')+obj.get('src')
				data.append(row)		

	main["headline"] = data
	return main

def matches(url='http://www.gosugamers.net/dota2/gosubet',limit=10):
	
	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'

	for div in soup_text.findAll('div'):
		if not div.attrs.has_key('class'): continue
		if not 'container' in div.attrs['class']: continue
		for obj in div.findAll('a'):
			if len(data) >= limit: break
			if not obj.attrs.has_key('class'): continue
			if not ('match' in obj.attrs['class'] and 'hover-background' in obj.attrs['class']): continue
			lineArray = []
			for line in obj.text.split('\n'):
				if not line != '': continue
				lineArray.append(line)
			data.append({
				"team1" : str(lineArray[0]),
				"team2" : str(lineArray[-1]),
				"team1pct" : str(lineArray[1]),
				"team2pct" : str(lineArray[3]),
				"href" : 'http://www.gosugamers.net' +obj.get("href")
			})
	main["matches"] = data
	return main


def rankings(url='http://www.gosugamers.net/dota2/rankings',limit=20):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'

	for div in soup_text.findAll('div'):
		if not div.attrs.has_key('class'): continue
		if not 'container' in div.attrs['class']: continue
		for obj in div.findAll('tr'):
			if len(data) >= limit: break
			lineArray = []
			for obj2 in obj.findAll('td'):
				line = re.sub(" ","",str(obj2.text).strip('\n'))
				if not str(line) != "": continue
				lineArray.append(line)
			if len(lineArray) < 3: continue
			data.append({
				"rank" : str(lineArray[0]),
				"teamname" : str(lineArray[1]),
				"score" : str(lineArray[2])
			})
	main['rankings'] = data
	return main

def hero_statistics(url='http://www.gosugamers.net/dota2/hero-stats'):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'
	
	return main

def events(url='http://www.gosugamers.net/events'):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'

	return main
