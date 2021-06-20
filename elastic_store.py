#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"

if __name__== '__main__':
	es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)
	query = {"query":{"bool":{"must":[{"match":{"site":"diningcode"}}]}}}
	lst =[]
	while True:
		try:
			docs = es.search(index='shop', body=query, size=10)
			break
		except Exception as e:
			print(1)
			continue
	if docs['hits']['total']['value']>0:	
		for doc in docs['hits']['hits']:
			print(doc['_source'])
			tmp = list(doc['_source'].values())
			print(tmp)
			lst.append(tmp)
	print(lst)
