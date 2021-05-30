#!/usr/bin/python3 
#-*- coding:utf-8 -*- 

import sys 
import re 
import requests 
from bs4 import BeautifulSoup 
from konlpy.tag import Kkma 
from elasticsearch import Elasticsearch 

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

  es_host="127.0.0.1" 
  es_port="9200" 

  es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30) 
  es.info() 

  def make_index(es, index_name): 
    if es.indices.exists(index=index_name): 
      es.indices.delete(index=index_name) 
    print(es.indices.create(index=index_name)) 

  index_name = 'tripadvisor' 
  make_index(es, index_name) 
  for i in range(0,5): 
    d = {} 
    d['name'] = l[i] 
    res = es.index(index=index_name, doc_type='string', body = d) 
  es.indices.refresh(index=index_name) 

result = es.search(index=index_name, body={'from':0, 'size':15, 'query':{'match':{'name':'레스토랑'}}}) 
