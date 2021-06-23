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




es_host="127.0.0.1"
es_port="9200"

def score_float(list):
	for i in range(0,len(list)):
		list[i][4] = float(list[i][4])
	return list
def score_str(list):
	for i in range(0,len(list)):
		list[i][4] = str(list[i][4])
	return list

def mk_para(list, f_list):
	for i in range(0,len(list)):
		str = ""
		str = "사이트:" + list[i][0] + " /"
		str = str + "가게이름:" + list[i][1] + " /"
		str = str + "주소:" + list[i][2] + " /"
		str = str + "메뉴:" + list[i][3] + " /"
		str = str + "별점:" + list[i][4] + " /"
		f_list.append(str)
	return f_list

#######################Elastic search START####################################
###############################################################################
es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)
query1 = {"query":{"bool":{"must":[{"match":{"site":"siksin"}}]}}}
query2 = {"query":{"bool":{"must":[{"match":{"site":"trip"}}]}}}
query3 = {"query":{"bool":{"must":[{"match":{"site":"d_code"}}]}}}
queryn = {"query":{"bool":{"must":[{"match":{"s_ad":"북구"}}]}}}
querys = {"query":{"bool":{"must":[{"match":{"s_ad":"남구"}}]}}}
queryss = {"query":{"bool":{"must":[{"match":{"s_ad":"수성구"}}]}}}
querye = {"query":{"bool":{"must":[{"match":{"s_ad":"동구"}}]}}}
queryw = {"query":{"bool":{"must":[{"match":{"s_ad":"서구"}}]}}}
querym = {"query":{"bool":{"must":[{"match":{"s_ad":"중구"}}]}}}
queryds = {"query":{"bool":{"must":[{"match":{"s_ad":"달서구"}}]}}}


	
north = []
east = []
west = []
ssung = []
south = []
mid = []
ds = []
#north
while True:
	try:
		docs = es.search(index='d_code', body=queryn, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		north.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=queryn, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		north.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=queryn, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		north.append(tmp)
while True:
	try:
		docs = es.search(index='menu', body=queryn, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		north.append(tmp)
print(north)
#west
while True:
	try:
		docs = es.search(index='d_code', body=queryw, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		west.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=queryw, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		west.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=queryw, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		west.append(tmp)
while True:
	try:
		docs = es.search(index='menu', body=queryw, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		west.append(tmp)
#수성
while True:
	try:
		docs = es.search(index='d_code', body=queryss, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ssung.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=queryss, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ssung.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=queryss, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ssung.append(tmp)
while True:
	try:
		docs = es.search(index='menu', body=queryss, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ssung.append(tmp)
print("수성구")
print(ssung)
#동구
while True:
	try:
		docs = es.search(index='d_code', body=querye, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		east.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=querye, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		east.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=querye, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		east.append(tmp)
while True:
	try:
		docs = es.search(index='menu', body=querye, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		east.append(tmp)
print("east")
print(east)
#남구
while True:
	try:
		docs = es.search(index='d_code', body=querys, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		south.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=querys, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		south.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=querys, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		south.append(tmp)
while True:
	try:
		docs = es.search(index='menu', body=querys, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		south.append(tmp)
print("south")
print(south)
#mid
while True:
	try:
		docs = es.search(index='d_code', body=querym, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		mid.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=querym, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		mid.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=querym, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		mid.append(tmp)
while True:
	try:
		docs = es.search(index='menu', body=querym, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		mid.append(tmp)
print("중구")
print(mid)
#달서
while True:
	try:
		docs = es.search(index='d_code', body=queryds, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ds.append(tmp)
while True:
	try:
		docs = es.search(index='siksin', body=queryds, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ds.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=queryds, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ds.append(tmp)
		print(ds)
while True:
	try:
		docs = es.search(index='menu', body=queryds, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		ds.append(tmp)
print("달서구")
print(ds)
north_f = []
east_f = []
west_f = []
ssung_f = []
south_f = []
mid_f =[]
ds_f = []
north = score_float(north)
north.sort(key=lambda x:-x[4])
north = score_str(north)
east = score_float(east)
east.sort(key=lambda x:-x[4])
east = score_str(east)
west = score_float(west)
west.sort(key=lambda x:-x[4])
west = score_str(west)
ds = score_float(ds)
ds.sort(key=lambda x:-x[4])
ds = score_str(ds)
ssung = score_float(ssung)
ssung.sort(key=lambda x:-x[4])
ssung = score_str(ssung)

south = score_float(south)
south.sort(key=lambda x:-x[4])
south = score_str(south)
mid = score_float(mid)
mid.sort(key=lambda x:-x[4])
mid = score_str(mid)

north_f = mk_para(north,north_f)
east_f = mk_para(east,east_f)
west_f= mk_para(west,west_f)
ssung_f = mk_para(ssung,ssung_f)
south_f = mk_para(south,south_f)
mid_f = mk_para(mid, mid_f)
ds_f = mk_para(ds, ds_f)
north_l = len(north)
east_l = len(east_f)
west_l = len(west_f)
ssung_l = len(ssung_f)
south_l = len(south_f)
mid_l = len(mid_f)
ds_l = len(ds_f)
print(north_l)
print(east_l)
print(west_l)
print(ssung_l)
print(south_l)
print(mid_l)
print(ds_l)

#######################Elastic search END######################################
###############################################################################


app = Flask(__name__)
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/info', methods=['GET'])
def info():
	error = None
	if request.method == 'GET':

		myname = request.args.get('rating')
	
		return render_template('info.html', name=myname,nor=north_f, est = east_f, wst = west_f, soo = ssung_f, sth = south_f, middle = mid_f, dsg = ds_f, nl = north_l,  el = east_l, wl = west_l, ssl = ssung_l, sl = south_l, ml = mid_l, dsl = ds_l)




if __name__=="__main__":
	app.run(debug=True)
	app.run(host="127.0.0.1", port="5000", debug=True)

