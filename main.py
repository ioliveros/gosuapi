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
		if div.attrs.has_key('class'):
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
			match = {}
			match["team1"] = str(lineArray[0])
			match["team2"] = str(lineArray[-1])
			match["team1pct"] = str(lineArray[1])
			match["team2pct"] = str(lineArray[3])
			match["href"] = 'http://www.gosugamers.net' +obj.get("href")
			data.append(match)

	main["matches"] = data
	return main


def rankings(url='http://www.gosugamers.net/dota2/rankings'):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'

	return main

def hero_statistics(url='http://www.gosugamers.net/dota2/hero-stats'):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'

	return main

def events(url='http://www.gosugamers.net/events'):

	soup_text,main,data = web_bsoupify(url),{},[]
	if not soup_text: return url + ': error in web api call, try again later'

	return main

if __name__ == '__main__':
	print headlines()
	#print matches()
	#print rankings()
	#print hero_statistics()
	#print events()
