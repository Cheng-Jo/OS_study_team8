#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma


def hfilter(s):
	return re.sub(u'[^\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':
	kkma = Kkma()
	word_d = {}
	req = requests.get('https://www.diningcode.com/list.php?query=%EA%B2%BD%EB%8C%80%EB%B6%81%EB%AC%B8')
	soup = BeautifulSoup(req.content, 'html.parser')

	html_title = soup.find_all(class_='btxt')
	#html_point = soup.find_all(class_='point')
	title = []
	#point = []
	for i in range(len(html_title)):
		title.append(hfilter(str(html_title[i])))
		#point.append(hfilter(str(html_point[i])))
	#d = {}
	#for i in range(len(title)):
	#	d[title[i]] = point[i]
	#print(d)
	print(title)
