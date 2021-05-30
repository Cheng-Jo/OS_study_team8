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
  res = requests.get('https://www.mangoplate.com/search/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C') 
  soup = BeautifulSoup(res.content, 'html.parser') 
  print(soup) 
