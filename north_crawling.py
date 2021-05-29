#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma

url = u'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=경북대+북문+맛집'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

l = []
area = soup.find_all(class_='info_area')

for item in area:
  d = {}
  d['name'] = item.find('a')['title']
  d['address'] = item.find(class_= "txt address").get_text()
  d['rating'] = item.find(class_= "rating").get_text()
  print(d)
