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
	return re.sub(u'[^\,\.\d\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
es_host="127.0.0.1"
es_port="9200"

if __name__== '__main__':
	kkma = Kkma()
	req1 = requests.get('https://www.siksinhot.com/search?keywords=%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C')
	soup1 = BeautifulSoup(req1.content, 'html.parser')
	pname = soup1.find_all(class_='store')
	siksin = []
	for i in range(0,5):
		siksin.append(nfilter(str(pname[i])))
	
	req2 = requests.get('https://www.diningcode.com/list.php?query=%EB%8C%80%EA%B5%AC')
	html = req2.text
	soup2 = BeautifulSoup(html, 'html.parser')
	d_code = []
	for i in range(0,5):
		d_code.append(soup2.find_all("span","btxt")[i].get_text())
		d_code[i] = d_code[i][3:]
	res3 = requests.get('https://www.tripadvisor.co.kr/Restaurants-g297886-Daegu.html') 
	soup3 = BeautifulSoup(res3.content, 'html.parser') 
	name = soup3.find_all('a', '_15_ydu6b') 
	trip = [] 
	cnt = 0 
	for i in name: 
		if cnt >= 5: 
			break 
		n = i.get_text() 
		k = n.split() 
		del k[0] 
		j = "".join(k) 
		trip.append(j) 
		cnt += 1
	es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)
	print(siksin)
	print(trip)
	print(d_code)
	for i in range(0,5):
		e1={
			"site":"siksin",
			"name":siksin[i].encode('utf-8'),
			"address":"남구"
		}
		res = es.index(index='siksin', doc_type='sik', id = i, body =e1)
		print(res)
	for i in range(0,5):
		e2={
			"site":"trip",
			"name":trip[i].encode('utf-8'),
			"address":"북구"
		}
		res2 = es.index(index='trip', doc_type='tri', id = i, body =e2)
		print(res2)
	for i in range(0,5):
		e={
			"site":"d_code",
			"name":d_code[i].encode('utf-8'),
			"address":"달서구"
		}
		if i < 3:
			e={
				"site":"d_code",
				"name":d_code[i].encode('utf-8'),
				"address":"남구"
			}
		else:
			e={
				"site":"d_code",
				"name":d_code[i].encode('utf-8'),
				"address":"북구"
			}


		res = es.index(index='d_code', doc_type='code', id = i, body =e)
		print(res)

