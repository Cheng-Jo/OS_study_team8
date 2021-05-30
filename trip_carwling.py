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
  res = requests.get('https://www.tripadvisor.co.kr/Restaurants-g297886-Daegu.html') 
  soup = BeautifulSoup(res.content, 'html.parser') 
  name = soup.find_all('a', '_15_ydu6b') 

  l = [] 
  cnt = 0 
  for i in name: 
    if cnt >= 5: 
      break 
    n = i.get_text() 
    k = n.split() 
    del k[0] 
    j = "".join(k) 
    l.append(j) 
    cnt += 1
  print(l) 
