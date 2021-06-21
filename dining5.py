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
  req = requests.get('https://www.diningcode.com/list.php?query=%EB%8C%80%EA%B5%AC') 
  html = req.text 
  soup = BeautifulSoup(html, 'html.parser') 

  d_code = [] 
  d_address = [] 
  d_menu = [] 
  d_point = [] 

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
