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
	req = requests.get('https://www.siksinhot.com/search?keywords=%EB%8C%80%EA%B5%AC%20Best%20%EB%A7%9B%EC%A7%91')
	soup = BeautifulSoup(req.content, 'html.parser')
	html_pname = soup.find_all(class_='store')
	html_pscore = soup.find_all(class_='score')
	pname = []
	pscore = []
	plocation = ['대구광역시 중구 동성로3가 59-1', '대구광역시 중구 공평동 56-3', '대구광역시 남구 대명동 1922-7', '대구광역시 동구 신암동 596-4', '대구광역시 북구 대현동 20-22']
	for i in range(5):
		html_pscore[i] = hfilter(str(html_pscore[i]))
		html_pscore[i] = html_pscore[i][3:]
		pname.append(nfilter(str(html_pname[i])))
		pscore.append(html_pscore[i])
	print(pname)
	print(pscore)
	print(plocation)

