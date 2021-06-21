#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"

	
if __name__== '__main__':
	es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)
	query1 = {"query":{"bool":{"must":[{"match":{"site":"siksin"}}]}}}
	query2 = {"query":{"bool":{"must":[{"match":{"site":"trip"}}]}}}
	query3 = {"query":{"bool":{"must":[{"match":{"site":"d_code"}}]}}}
	queryn = {"query":{"bool":{"must":[{"match":{"s_ad":"북구"}}]}}}
	querys = {"query":{"bool":{"must":[{"match":{"s_ad":"남구"}}]}}}
	queryss = {"query":{"bool":{"must":[{"match":{"s_ad":"수성구"}}]}}}
	querye = {"query":{"bool":{"must":[{"match":{"s_ad":"동구"}}]}}}
	queryw = {"query":{"bool":{"must":[{"match":{"s_ad":"서구"}}]}}}
	lst1 =[]
	lst2 =[]
	lst3 = []
	north = []
	east = []
	west = []
	ssung = []
	south = []
	while True:
		try:
			docs = es.search(index='siksin', body=query1, size=5)
			break
		except Exception as e:
			print('error')
			continue
	if docs['hits']['total']['value']>0:	
		for doc in docs['hits']['hits']:
			print(doc['_source'])
			tmp = list(doc['_source'].values())
			print(tmp)
			lst1.append(tmp)
#	print(lst1)
	while True:
		try:
			docs = es.search(index='trip', body=query2, size=5)
			break
		except Exception as e:
			print(1)
			continue
	if docs['hits']['total']['value']>0:
		for doc in docs['hits']['hits']:
			print(doc['_source'])
			tmp = list(doc['_source'].values())
			print(tmp)
			lst2.append(tmp)
#	print(lst2)
	while True:
		try:
			docs = es.search(index='d_code', body=query3, size=5)
			break
		except Exception as e:
			print(1)
			continue
	if docs['hits']['total']['value']>0:
		for doc in docs['hits']['hits']:
			print(doc['_source'])
			tmp = list(doc['_source'].values())
			print(tmp)
			lst3.append(tmp)
#	print(lst3)
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
	print(west)
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
	print(south)
