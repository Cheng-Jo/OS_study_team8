#!/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
from elasticsearch import Elasticsearch

es_host = "127.0.0.1"
es_port= "9200"

if __name__== '__main__':
	es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)
	req = requests.get('https://www.diningcode.com/list.php?query=%EB%8C%80%EA%B5%AC')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	tlist = []
	for i in range(0,10):
		tlist.append(soup.find_all("span","btxt")[i].get_text())
		tlist[i] = tlist[i][3:]
	print(tlist)
	for i in range(0,10):
		e={
        	        "name":tlist[i].encode('utf-8'),
		}

		res = es.index(index='shop', doc_type='haochi', id = i, body =e)
		print(res)
