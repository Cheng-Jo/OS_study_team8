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


	lst1 =[]
	lst2 =[]
	lst3 = []
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
	print(lst1)
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
	print(lst2)
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
	print(lst3)

