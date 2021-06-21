#!/usr/bin/python3
#-*- coding: utf-8 -*-
import argparse
import subprocess
from flask import Flask, jsonify
from flask import render_template
from flask import request
import re 
import requests 
from bs4 import BeautifulSoup 
from konlpy.tag import Kkma 
import sys
from elasticsearch import Elasticsearch

def hfilter(s):
	return re.sub(u'[^\ \,\.\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\?\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def hfilter2(s): 
	return re.sub(u'[^\,\.\d\?\!\u3130-\u318f\uac00-\ud7a3]+','',s) 
def nfilter2(s): 
	return re.sub(u'[^\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s) 
def f_address(adrress):
	s ="남구"
	w ="서구"
	e ="동구"
	n ="북구"
	ss = "수성구"
	m = "중구"
	tmp = adrress.split()
	for i in range(0, len(tmp)):
		print(tmp[i])
		if s in tmp[i]:
			return s
		elif w in tmp[i]:
			return w
		elif e in tmp[i]:
			return e
		elif n in tmp[i]:
			return n
		elif ss in tmp[i]:
			return ss
		elif m in tmp[i]:
			return m

es_host="127.0.0.1"
es_port="9200"

if __name__ == '__main__': 
	kkma = Kkma() 
	req1 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7010929-Reviews-Balaji_Restaurant-Daegu.html') 
	soup1 = BeautifulSoup(req1.text, 'html.parser') 

	trip_name = [] 
	trip_address = [] 
	trip_menu = [] 
	trip_point = [] 

	name = soup1.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup1.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address[3:]) 
	menu = soup1.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup1.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req2 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7943036-Reviews-Hi_Thai-Daegu.html') 
	soup2 = BeautifulSoup(req2.text, 'html.parser') 
	name = soup2.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup2.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address[3:]) 
	menu = soup2.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup2.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req3 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d10218361-Reviews-Deira_Restaurant-Daegu.html') 
	soup3 = BeautifulSoup(req3.text, 'html.parser') 
	name = soup3.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup3.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address[3:]) 
	menu = soup3.find_all("a", "_2mn01bsa") 
	trip_menu.append(menu[1].get_text()) 
	point = soup3.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req4 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7265417-Reviews-New_Saladdin-Daegu.html') 
	soup4 = BeautifulSoup(req4.text, 'html.parser') 
	name = soup4.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup4.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address[3:]) 
	menu = soup4.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup4.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req5 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d8055192-Reviews-Jungang_Tteokbokki-Daegu.html') 
	soup5 = BeautifulSoup(req5.text, 'html.parser') 
	name = soup5.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup5.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address[3:]) 
	menu = soup5.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup5.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	print(trip_name) 
	print(trip_address) 
	print(trip_menu) 
	print(trip_point) 
	print("trip end")
	name = []
	score = []
	location = []
	category = ['세계음식', '한국음식', '한국음식', '한국음식', '한국음식']
	
	req1 = requests.get('https://www.siksinhot.com/P/353339')
	soup1 = BeautifulSoup(req1.content, 'html.parser')

	html_name1 = soup1.find(id='title').get_text()
	html_score1 = soup1.find('strong').get_text()
	html_loc1 = soup1.find(class_ = "txt_adr").get_text()
	name.append(str(html_name1).strip())
	score.append(str(html_score1)[2:])
	location.append(str(html_loc1).strip()[6:])

	req2 = requests.get('https://www.siksinhot.com/P/269870')
	soup2 = BeautifulSoup(req2.content, 'html.parser')

	html_name2 = soup2.find(id='title').get_text()
	html_score2 = soup2.find('strong').get_text()
	html_loc2 = soup2.find(class_ = "txt_adr").get_text()
	name.append(str(html_name2).strip())
	score.append(str(html_score2)[2:])
	location.append(str(html_loc2).strip()[6:])

	req3 = requests.get('https://www.siksinhot.com/P/264776')
	soup3 = BeautifulSoup(req3.content, 'html.parser')

	html_name3 = soup3.find(id='title').get_text()
	html_score3 = soup3.find('strong').get_text()
	html_loc3 = soup3.find(class_ = "txt_adr").get_text()
	name.append(str(html_name3).strip()[6:])
	score.append(str(html_score3)[2:])
	location.append(str(html_loc3).strip())

	req4 = requests.get('https://www.siksinhot.com/P/268900')
	soup4 = BeautifulSoup(req4.content, 'html.parser')

	html_name4 = soup4.find(id='title').get_text()
	html_score4 = soup4.find('strong').get_text()
	html_loc4 = soup4.find(class_ = "txt_adr").get_text()
	name.append(str(html_name4).strip())
	score.append(str(html_score4)[2:])
	location.append(str(html_loc4).strip()[6:])

	req5 = requests.get('https://www.siksinhot.com/P/356055')
	soup5 = BeautifulSoup(req5.content, 'html.parser')

	html_name5 = soup5.find(id='title').get_text()
	html_score5 = soup5.find('strong').get_text()
	html_loc5 = soup5.find(class_ = "txt_adr").get_text()
	name.append(str(html_name5).strip()[6:])
	score.append(str(html_score5)[2:])
	location.append(str(html_loc5).strip())

	print(name)
	print(score)
	print(location)
	print(category)
	print("siksin end")

	m_name = []
	m_score = []
	m_location = []
	m_category = []

	req1 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=R700334')
	soup1 = BeautifulSoup(req1.content, 'html.parser')
	html_name1 = soup1.find(class_ = 'storeName').get_text()
	html_score1 = soup1.find(class_ = 'total').get_text()
	html_location1 = soup1.find(class_ = 'add1').get_text()
	html_category1 = soup1.find(class_ = 'type').get_text()
	m_name.append(html_name1)
	m_score.append(html_score1)
	m_location.append(html_location1[3:])
	m_category.append(html_category1)
	
	req2 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702258')
	soup2 = BeautifulSoup(req2.content, 'html.parser')
	html_name2 = soup2.find(class_ = 'storeName').get_text()
	html_score2 = soup2.find(class_ = 'total').get_text()
	html_location2 = soup2.find(class_ = 'add1').get_text() 
	html_category2 = soup2.find(class_ = 'type').get_text() 
	m_name.append(html_name2)
	m_score.append(html_score2)
	m_location.append(html_location2[3:])
	m_category.append(html_category2)
	
	req3 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702257')
	soup3 = BeautifulSoup(req3.content, 'html.parser')
	html_name3 = soup3.find(class_ = 'storeName').get_text()
	html_score3 = soup3.find(class_ = 'total').get_text()
	html_location3 = soup3.find(class_ = 'add1').get_text()
	html_category3 = soup3.find(class_ = 'type').get_text() 
	m_name.append(html_name3)
	m_score.append(html_score3)
	m_location.append(html_location3[3:])
	m_category.append(html_category3)
	
	req4 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702247')
	soup4 = BeautifulSoup(req4.content, 'html.parser')
	html_name4 = soup4.find(class_ = 'storeName').get_text()
	html_score4 = soup4.find(class_ = 'total').get_text()
	html_location4 = soup4.find(class_ = 'add1').get_text() 
	html_category4 = soup4.find(class_ = 'type').get_text() 
	m_name.append(html_name4)
	m_score.append(html_score4)
	m_location.append(html_location4[3:])
	m_category.append(html_category4)
	
	req5 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702251')
	soup5 = BeautifulSoup(req5.content, 'html.parser')
	html_name5 = soup5.find(class_ = 'storeName').get_text()
	html_score5 = soup5.find(class_ = 'total').get_text()
	html_location5 = soup5.find(class_ = 'add1').get_text() 
	html_category5 = soup5.find(class_ = 'type').get_text()
	m_name.append(html_name5)
	m_score.append(html_score5)
	m_location.append(html_location5[3:])
	m_category.append(html_category5)
	

	print(m_name)
	print(m_score)
	print(m_location)
	print(m_category)
	print("menu end")

	d_code = [] 
	d_address = [] 
	d_menu = [] 
	d_point = [] 

	req = requests.get('https://www.diningcode.com/list.php?query=%EB%8C%80%EA%B5%AC') 
	html = req.text 
	soup = BeautifulSoup(html, 'html.parser')
	for i in range(0,5): 
		d_code.append(soup.find_all("span","btxt")[i].get_text()) 
		d_menu.append(soup.find_all("span", "stxt")[i].get_text()) 
		d_code[i] = d_code[i][3:] 

	req1 = requests.get('https://www.diningcode.com/profile.php?rid=hq047MomVuaT') 
	soup1 = BeautifulSoup(req1.text, 'html.parser') 
	d_point.append(soup1.find_all("span", "point")[1].get_text()) 
	d_address.append(soup1.find("li","locat").get_text()[4:])

	req2 = requests.get('https://www.diningcode.com/profile.php?rid=OO6PTlAgMlnk') 
	soup2 = BeautifulSoup(req2.text, 'html.parser') 
	d_point.append(soup2.find_all("span", "point")[1].get_text()) 
	d_address.append(soup1.find("li","locat").get_text()[4:])

	req3 = requests.get('https://www.diningcode.com/profile.php?rid=gRC5ab8eUCWC') 
	soup3 = BeautifulSoup(req3.text, 'html.parser') 
	d_point.append(soup3.find_all("span", "point")[1].get_text()) 
	d_address.append(soup1.find("li","locat").get_text()[4:])

	req4 = requests.get('https://www.diningcode.com/profile.php?rid=haiJHpKMyHaM') 
	soup4 = BeautifulSoup(req4.text, 'html.parser') 
	d_point.append(soup4.find_all("span", "point")[1].get_text()) 
	d_address.append(soup1.find("li","locat").get_text()[4:])

	req5 = requests.get('https://www.diningcode.com/profile.php?rid=rlBuOzqmsy8y') 
	soup5 = BeautifulSoup(req5.text, 'html.parser') 
	d_point.append(soup5.find_all("span", "point")[1].get_text()) 
	d_address.append(soup1.find("li","locat").get_text()[4:])

	print(d_code) 
	print(d_address) 
	print(d_menu) 
	print(d_point) 
	print("dining end")
	es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)
	for i in range(0,5):
		s_ad1 = f_address(location[i])
		e1={
			"site":"siksin",
			"name":name[i].encode('utf-8'),
			"address":location[i],
			"category":category[i],
			"Score":score[i],
			"s_ad":s_ad1
		}
		res = es.index(index='siksin', doc_type='sik', id = i, body =e1)
		print(res)
	for i in range(0,5):
		s_ad2 = f_address(trip_address[i])
		e2={
			"site":"trip",
			"name":trip_name[i].encode('utf-8'),
			"address":trip_address[i],
			"category":trip_menu[i],
			"Score":trip_point[i],
			"s_ad":s_ad2

		}
		res2 = es.index(index='trip', doc_type='tri', id = i, body =e2)
		print(res2)
	for i in range(0,5):
		s_ad3 = f_address(d_address[i])
		e3={
			"site":"d_code",
			"name":d_code[i].encode('utf-8'),
			"address":d_address[i],
			"category":d_menu[i],
			"Score":d_point[i],
			"s_ad":s_ad3

		}


		res = es.index(index='d_code', doc_type='code', id = i, body =e3)
		print(res)
	for i in range(0,5):
		s_ad4 = f_address(m_location[i])
		e4={
			"site":"menupan",
			"name":m_name[i].encode('utf-8'),
			"address":m_location[i],
			"category":m_category[i],
			"Score":m_score[i],
			"s_ad":s_ad4

		}


		res = es.index(index='menu', doc_type='me', id = i, body =e4)
		print(res)
