#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma


def hfilter(s):
	return re.sub(u'[^\,\.\d\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':
	kkma = Kkma()
	word_d = {}
	req = requests.get('https://www.siksinhot.com/search?keywords=%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C')
	soup = BeautifulSoup(req.content, 'html.parser')
	html_pname = soup.find_all(class_='store')
	#html_score = soup.find_all(class_='score')
	#print(html_pname)
	#print(html_score)
	pname = []
	score = []
	for i in range(len(html_pname)):
		pname.append(nfilter(str(html_pname[i])))
	#	score.append(hfilter(str(html_score[i])))
	d = {}
	#for i in range(len(pname)):
	#	d[pname[i]] = score[i]
	#print(d)
	print(pname)
	#print(score)


