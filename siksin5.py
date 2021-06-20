#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
#from konlpy.tag import Kkma


def hfilter(s):
	return re.sub(u'[^\ \,\.\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\?\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':
	name = []
	score = []
	location = []
	category = ['세계음식', '한국음식', '한국음식', '한국음식', '한국음식']
	
	req1 = requests.get('https://www.siksinhot.com/P/353339')
	soup1 = BeautifulSoup(req1.content, 'html.parser')

	html_name1 = soup1.find(id='title')
	html_score1 = soup1.find('strong')
	html_loc1 = soup1.find_all(class_ = "txt_adr")
	name.append(hfilter(str(html_name1)).strip())
	score.append(nfilter(str(html_score1))[2:])
	location.append(hfilter(str(html_loc1)).strip())

	req2 = requests.get('https://www.siksinhot.com/P/269870')
	soup2 = BeautifulSoup(req2.content, 'html.parser')

	html_name2 = soup2.find(id='title')
	html_score2 = soup2.find('strong')
	html_loc2 = soup2.find_all(class_ = "txt_adr")
	name.append(hfilter(str(html_name2)).strip())
	score.append(nfilter(str(html_score2))[2:])
	location.append(hfilter(str(html_loc2)).strip())

	req3 = requests.get('https://www.siksinhot.com/P/264776')
	soup3 = BeautifulSoup(req3.content, 'html.parser')

	html_name3 = soup3.find(id='title')
	html_score3 = soup3.find('strong')
	html_loc3 = soup3.find_all(class_ = "txt_adr")
	name.append(hfilter(str(html_name3)).strip())
	score.append(nfilter(str(html_score3))[2:])
	location.append(hfilter(str(html_loc3)).strip())

	req4 = requests.get('https://www.siksinhot.com/P/268900')
	soup4 = BeautifulSoup(req4.content, 'html.parser')

	html_name4 = soup4.find(id='title')
	html_score4 = soup4.find('strong')
	html_loc4 = soup4.find_all(class_ = "txt_adr")
	name.append(hfilter(str(html_name4)).strip())
	score.append(nfilter(str(html_score4))[2:])
	location.append(hfilter(str(html_loc4)).strip())

	req5 = requests.get('https://www.siksinhot.com/P/356055')
	soup5 = BeautifulSoup(req5.content, 'html.parser')

	html_name5 = soup5.find(id='title')
	html_score5 = soup5.find('strong')
	html_loc5 = soup5.find_all(class_ = "txt_adr")
	name.append(hfilter(str(html_name5)).strip())
	score.append(nfilter(str(html_score5))[2:])
	location.append(hfilter(str(html_loc5)).strip())

	print(name)
	print(score)
	print(location)
	print(category)
