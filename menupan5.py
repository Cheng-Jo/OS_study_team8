#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup


def hfilter(s):
	return re.sub(u'[^\ \-\,\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def kgwfilter(s):
	return re.sub(u'[^\d\ \-\|\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':
	name = []
	score = []
	location = []
	category = []

	req1 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=R700334')
	soup1 = BeautifulSoup(req1.content, 'html.parser')
	html_name1 = soup1.find(class_ = 'storeName')
	html_score1 = soup1.find(class_ = 'total')
	html_location1 = soup1.find(class_ = 'add1')
	html_category1 = soup1.find(class_ = 'type')
	name.append(hfilter(str(html_name1)).strip())
	score.append(nfilter(str(html_score1)))
	location.append(hfilter(str(html_location1)).strip()[10:])
	category.append(hfilter(str(html_category1)).strip())
	
	req2 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702258')
	soup2 = BeautifulSoup(req2.content, 'html.parser')
	html_name2 = soup2.find(class_ = 'storeName')
	html_score2 = soup2.find(class_ = 'total')
	html_location2 = soup2.find(class_ = 'add1') 
	html_category2 = soup2.find(class_ = 'type') 
	name.append(hfilter(str(html_name2)).strip())
	score.append(nfilter(str(html_score2)))
	location.append(hfilter(str(html_location2)).strip()[10:])
	category.append(hfilter(str(html_category2)).strip())
	
	req3 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702257')
	soup3 = BeautifulSoup(req3.content, 'html.parser')
	html_name3 = soup3.find(class_ = 'storeName')
	html_score3 = soup3.find(class_ = 'total')
	html_location3 = soup3.find(class_ = 'add1') 
	html_category3 = soup3.find(class_ = 'type') 
	name.append(hfilter(str(html_name3)).strip())
	score.append(nfilter(str(html_score3)))
	location.append(hfilter(str(html_location3)).strip()[10:])
	category.append(hfilter(str(html_category3)).strip())
	
	req4 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702247')
	soup4 = BeautifulSoup(req4.content, 'html.parser')
	html_name4 = soup4.find(class_ = 'storeName')
	html_score4 = soup4.find(class_ = 'total')
	html_location4 = soup4.find(class_ = 'add1') 
	html_category4 = soup4.find(class_ = 'type') 
	name.append(hfilter(str(html_name4)).strip())
	score.append(nfilter(str(html_score4)))
	location.append(hfilter(str(html_location4)).strip()[10:])
	category.append(hfilter(str(html_category4)).strip())
	
	req5 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702251')
	soup5 = BeautifulSoup(req5.content, 'html.parser')
	html_name5 = soup5.find(class_ = 'storeName')
	html_score5 = soup5.find(class_ = 'total')
	html_location5 = soup5.find(class_ = 'add1') 
	html_category5 = soup5.find(class_ = 'type') 
	name.append(hfilter(str(html_name5)).strip())
	score.append(nfilter(str(html_score5)))
	location.append(hfilter(str(html_location5)).strip()[10:])
	category.append(hfilter(str(html_category5)).strip())
	

	print(name)
	print(score)
	print(location)
	print(category)
