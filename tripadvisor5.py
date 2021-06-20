#!/usr/bin/python3 
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
  trip_point.append(hfilter(point)) 

  req2 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7943036-Reviews-Hi_Thai-Daegu.html') 
  soup2 = BeautifulSoup(req2.text, 'html.parser') 
  name = soup2.find_all("h1") 
  trip_name.append(name[1].get_text()) 
  address = soup2.find("span", "_2saB_OSe").get_text() 
  trip_address.append(address) 
  menu = soup2.find("div", "_1XLfiSsv").get_text() 
  trip_menu.append(menu) 
  point = soup2.find("span", "r2Cf69qf").get_text() 
  trip_point.append(hfilter(point)) 

  req3 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d10218361-Reviews-Deira_Restaurant-Daegu.html') 
  soup3 = BeautifulSoup(req3.text, 'html.parser') 
  name = soup3.find_all("h1") 
  trip_name.append(name[1].get_text()) 
  address = soup3.find("span", "_2saB_OSe").get_text() 
  trip_address.append(address) 
  menu = soup3.find_all("a", "_2mn01bsa") 
  trip_menu.append(menu[1].get_text()) 
  point = soup3.find("span", "r2Cf69qf").get_text() 
  trip_point.append(hfilter(point)) 

  req4 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7265417-Reviews-New_Saladdin-Daegu.html') 
  soup4 = BeautifulSoup(req4.text, 'html.parser') 
  name = soup4.find_all("h1") 
  trip_name.append(name[1].get_text()) 
  address = soup4.find("span", "_2saB_OSe").get_text() 
  trip_address.append(address) 
  menu = soup4.find("div", "_1XLfiSsv").get_text() 
  trip_menu.append(menu) 
  point = soup4.find("span", "r2Cf69qf").get_text() 
  trip_point.append(hfilter(point)) 

  req5 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d8055192-Reviews-Jungang_Tteokbokki-Daegu.html') 
  soup5 = BeautifulSoup(req5.text, 'html.parser') 
  name = soup5.find_all("h1") 
  trip_name.append(name[1].get_text()) 
  address = soup5.find("span", "_2saB_OSe").get_text() 
  trip_address.append(address) 
  menu = soup5.find("div", "_1XLfiSsv").get_text() 
  trip_menu.append(menu) 
  point = soup5.find("span", "r2Cf69qf").get_text() 
  trip_point.append(hfilter(point)) 

  print(trip_name) 
  print(trip_address) 
  print(trip_menu) 
  print(trip_point) 
