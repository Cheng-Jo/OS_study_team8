#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma


def hfilter(s):
	return re.sub(u'[^\,\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def kgwfilter(s):
	return re.sub(u'[^\d\ \-\|\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':
	kkma = Kkma()
	word_d = {}
	req = requests.get('https://www.menupan.com/search/restaurant/restaurant_result.asp?sc=basicdata&kw=%B4%EB%B1%B8%B1%A4%BF%AA%BD%C3')
	soup = BeautifulSoup(req.content, 'html.parser')
	html_pname = soup.find_all(target = '_blank')
	html_plocation = soup.find_all(class_ = 'sum')
	pname = []
	plocation = []
	for i in range(5):
		pname.append(nfilter(str(html_pname[22 + 2*i])))

		html_plocation[i] = kgwfilter(str(html_plocation[i]))
		plocation.append(html_plocation[i][:html_plocation[i].index('|')])
	print(pname)
	print(plocation)

