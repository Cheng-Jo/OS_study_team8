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
  d_point = [] 

  for i in range(0,5): 
    d_code.append(soup.find_all("span","btxt")[i].get_text()) 
    d_address.append(soup.find_all("span","ctxt")[2 * i + 1].get_text()) 
    d_point.append(soup.find_all("span", "point")[i].get_text()) 
    d_code[i] = d_code[i][3:] 
    d_address[i] = d_address[i][2:] 
