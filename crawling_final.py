#!/usr/bin/python3 
#-*- coding:utf-8 -*- 

import re 
import requests 
from bs4 import BeautifulSoup 
from konlpy.tag import Kkma 

def hfilter(s):
	return re.sub(u'[^\ \,\.\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\?\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def hfilter2(s): 
	return re.sub(u'[^\,\.\d\?\!\u3130-\u318f\uac00-\ud7a3]+','',s) 
def nfilter2(s): 
	return re.sub(u'[^\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s) 

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
	trip_address.append(address) 
	menu = soup1.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup1.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req2 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7943036-Reviews-Hi_Thai-Daegu.html') 
	soup2 = BeautifulSoup(req2.text, 'html.parser') 
	name = soup2.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup2.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address) 
	menu = soup2.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup2.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req3 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d10218361-Reviews-Deira_Restaurant-Daegu.html') 
	soup3 = BeautifulSoup(req3.text, 'html.parser') 
	name = soup3.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup3.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address) 
	menu = soup3.find_all("a", "_2mn01bsa") 
	trip_menu.append(menu[1].get_text()) 
	point = soup3.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req4 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7265417-Reviews-New_Saladdin-Daegu.html') 
	soup4 = BeautifulSoup(req4.text, 'html.parser') 
	name = soup4.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup4.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address) 
	menu = soup4.find("div", "_1XLfiSsv").get_text() 
	trip_menu.append(menu) 
	point = soup4.find("span", "r2Cf69qf").get_text() 
	trip_point.append(hfilter2(point)) 

	req5 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d8055192-Reviews-Jungang_Tteokbokki-Daegu.html') 
	soup5 = BeautifulSoup(req5.text, 'html.parser') 
	name = soup5.find_all("h1") 
	trip_name.append(name[1].get_text()) 
	address = soup5.find("span", "_2saB_OSe").get_text() 
	trip_address.append(address) 
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
	print("siksin end")

	m_name = []
	m_score = []
	m_location = []
	m_category = []

	req1 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=R700334')
	soup1 = BeautifulSoup(req1.content, 'html.parser')
	html_name1 = soup1.find(class_ = 'storeName')
	html_score1 = soup1.find(class_ = 'total')
	html_location1 = soup1.find(class_ = 'add1')
	html_category1 = soup1.find(class_ = 'type')
	m_name.append(hfilter(str(html_name1)).strip())
	m_score.append(nfilter(str(html_score1)))
	m_location.append(hfilter(str(html_location1)).strip()[10:])
	m_category.append(hfilter(str(html_category1)).strip())
	
	req2 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702258')
	soup2 = BeautifulSoup(req2.content, 'html.parser')
	html_name2 = soup2.find(class_ = 'storeName')
	html_score2 = soup2.find(class_ = 'total')
	html_location2 = soup2.find(class_ = 'add1') 
	html_category2 = soup2.find(class_ = 'type') 
	m_name.append(hfilter(str(html_name2)).strip())
	m_score.append(nfilter(str(html_score2)))
	m_location.append(hfilter(str(html_location2)).strip()[10:])
	m_category.append(hfilter(str(html_category2)).strip())
	
	req3 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702257')
	soup3 = BeautifulSoup(req3.content, 'html.parser')
	html_name3 = soup3.find(class_ = 'storeName')
	html_score3 = soup3.find(class_ = 'total')
	html_location3 = soup3.find(class_ = 'add1') 
	html_category3 = soup3.find(class_ = 'type') 
	m_name.append(hfilter(str(html_name3)).strip())
	m_score.append(nfilter(str(html_score3)))
	m_location.append(hfilter(str(html_location3)).strip()[10:])
	m_category.append(hfilter(str(html_category3)).strip())
	
	req4 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702247')
	soup4 = BeautifulSoup(req4.content, 'html.parser')
	html_name4 = soup4.find(class_ = 'storeName')
	html_score4 = soup4.find(class_ = 'total')
	html_location4 = soup4.find(class_ = 'add1') 
	html_category4 = soup4.find(class_ = 'type') 
	m_name.append(hfilter(str(html_name4)).strip())
	m_score.append(nfilter(str(html_score4)))
	m_location.append(hfilter(str(html_location4)).strip()[10:])
	m_category.append(hfilter(str(html_category4)).strip())
	
	req5 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702251')
	soup5 = BeautifulSoup(req5.content, 'html.parser')
	html_name5 = soup5.find(class_ = 'storeName')
	html_score5 = soup5.find(class_ = 'total')
	html_location5 = soup5.find(class_ = 'add1') 
	html_category5 = soup5.find(class_ = 'type') 
	m_name.append(hfilter(str(html_name5)).strip())
	m_score.append(nfilter(str(html_score5)))
	m_location.append(hfilter(str(html_location5)).strip()[10:])
	m_category.append(hfilter(str(html_category5)).strip())
	

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
		d_address.append(soup.find_all("span","ctxt")[2 * i + 1].get_text()) 
		d_menu.append(soup.find_all("span", "stxt")[i].get_text()) 
		d_code[i] = d_code[i][3:] 
		d_address[i] = d_address[i][2:] 

	req1 = requests.get('https://www.diningcode.com/profile.php?rid=hq047MomVuaT') 
	soup1 = BeautifulSoup(req1.text, 'html.parser') 
	d_point.append(soup1.find_all("span", "point")[1].get_text()) 

	req2 = requests.get('https://www.diningcode.com/profile.php?rid=OO6PTlAgMlnk') 
	soup2 = BeautifulSoup(req2.text, 'html.parser') 
	d_point.append(soup2.find_all("span", "point")[1].get_text()) 

	req3 = requests.get('https://www.diningcode.com/profile.php?rid=gRC5ab8eUCWC') 
	soup3 = BeautifulSoup(req3.text, 'html.parser') 
	d_point.append(soup3.find_all("span", "point")[1].get_text()) 

	req4 = requests.get('https://www.diningcode.com/profile.php?rid=haiJHpKMyHaM') 
	soup4 = BeautifulSoup(req4.text, 'html.parser') 
	d_point.append(soup4.find_all("span", "point")[1].get_text()) 

	req5 = requests.get('https://www.diningcode.com/profile.php?rid=rlBuOzqmsy8y') 
	soup5 = BeautifulSoup(req5.text, 'html.parser') 
	d_point.append(soup5.find_all("span", "point")[1].get_text()) 

	print(d_code) 
	print(d_address) 
	print(d_menu) 
	print(d_point) 
	print("dining end")
