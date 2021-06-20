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



def kgwfilter(s):
	return re.sub(u'[^\d\ \-\|\u3130-\u318f\uac00-\ud7a3]+','',s)

def hfilter(s):
	return re.sub(u'[^\ \,\.\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\?\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)


es_host="127.0.0.1"
es_port="9200"


#######################Crawling START##########################################
###############################################################################


###siksin crawling###
#####################
siksin_name = []
siksin_score = []
siksin_location = []
siksin_category = ['세계음식', '한국음식', '한국음식', '한국음식', '한국음식']

siksin_req1 = requests.get('https://www.siksinhot.com/P/353339')
siksin_soup1 = BeautifulSoup(siksin_req1.content, 'html.parser')
siksin_html_name1 = siksin_soup1.find(id='title')
siksin_html_score1 = siksin_soup1.find('strong')
siksin_html_loc1 = siksin_soup1.find_all(class_ = "txt_adr")
siksin_name.append(hfilter(str(siksin_html_name1)).strip())
siksin_score.append(nfilter(str(siksin_html_score1))[2:])
siksin_location.append(hfilter(str(siksin_html_loc1)).strip())

siksin_req2 = requests.get('https://www.siksinhot.com/P/269870')
siksin_soup2 = BeautifulSoup(siksin_req2.content, 'html.parser')
siksin_html_name2 = siksin_soup2.find(id='title')
siksin_html_score2 = siksin_soup2.find('strong')
siksin_html_loc2 = siksin_soup2.find_all(class_ = "txt_adr")
siksin_name.append(hfilter(str(siksin_html_name2)).strip())
siksin_score.append(nfilter(str(siksin_html_score2))[2:])
siksin_location.append(hfilter(str(siksin_html_loc2)).strip())

siksin_req3 = requests.get('https://www.siksinhot.com/P/264776')
siksin_soup3 = BeautifulSoup(siksin_req3.content, 'html.parser')
siksin_html_name3 = siksin_soup3.find(id='title')
siksin_html_score3 = siksin_soup3.find('strong')
siksin_html_loc3 = siksin_soup3.find_all(class_ = "txt_adr")
siksin_name.append(hfilter(str(siksin_html_name3)).strip())
siksin_score.append(nfilter(str(siksin_html_score3))[2:])
siksin_location.append(hfilter(str(siksin_html_loc3)).strip())

siksin_req4 = requests.get('https://www.siksinhot.com/P/268900')
siksin_soup4 = BeautifulSoup(siksin_req4.content, 'html.parser')
siksin_html_name4 = siksin_soup4.find(id='title')
siksin_html_score4 = siksin_soup4.find('strong')
siksin_html_loc4 = siksin_soup4.find_all(class_ = "txt_adr")
siksin_name.append(hfilter(str(siksin_html_name4)).strip())
siksin_score.append(nfilter(str(siksin_html_score4))[2:])
siksin_location.append(hfilter(str(siksin_html_loc4)).strip())

siksin_req5 = requests.get('https://www.siksinhot.com/P/356055')
siksin_soup5 = BeautifulSoup(siksin_req5.content, 'html.parser')
siksin_html_name5 = siksin_soup5.find(id='title')
siksin_html_score5 = siksin_soup5.find('strong')
siksin_html_loc5 = siksin_soup5.find_all(class_ = "txt_adr")
siksin_name.append(hfilter(str(siksin_html_name5)).strip())
siksin_score.append(nfilter(str(siksin_html_score5))[2:])
siksin_location.append(hfilter(str(siksin_html_loc5)).strip())
#####################
#####################

###d_code crawling###
#####################
kkma = Kkma() 
req = requests.get('https://www.diningcode.com/list.php?query=%EB%8C%80%EA%B5%AC') 
html = req.text 
soup = BeautifulSoup(html, 'html.parser') 
d_code = []
d_point = []
d_menu = []
d_address = []

for i in range(0,5):
	d_code.append(soup.find_all("span","btxt")[i].get_text()) 
	d_address.append(soup.find_all("span","ctxt")[2 * i + 1].get_text()) 
	d_menu.append(soup.find_all("span", "stxt")[i].get_text()) 
	d_code[i] = d_code[i][3:] 
	d_address[i] = d_address[i][2:] 
req1 = requests.get('https://www.diningcode.com/profile.php?rid=hq047MomVuaT') 
soup1 = BeautifulSoup(req1.text, 'html.parser') 
d_point.append(soup1.find_all("span", "point")[1].get_text()) 
req2 = requests.get('https://www.diningcode.com/profile.php?rid=OO6PTlAgMlnk') 
soup2 = BeautifulSoup(req2.text, 'html.parser') 
d_point.append(soup2.find_all("span", "point")[1].get_text()) 
req3 = requests.get('https://www.diningcode.com/profile.php?rid=gRC5ab8eUCWC') 
soup3 = BeautifulSoup(req3.text, 'html.parser') 
d_point.append(soup3.find_all("span", "point")[1].get_text()) 
req4 = requests.get('https://www.diningcode.com/profile.php?rid=haiJHpKMyHaM') 
soup4 = BeautifulSoup(req4.text, 'html.parser') 
d_point.append(soup4.find_all("span", "point")[1].get_text()) 
req5 = requests.get('https://www.diningcode.com/profile.php?rid=rlBuOzqmsy8y') 
soup5 = BeautifulSoup(req5.text, 'html.parser') 
d_point.append(soup5.find_all("span", "point")[1].get_text()) 
#####################
#####################

###trip_adCrawling###
#####################
def hfilter(s): 
	return re.sub(u'[^\,\.\d\?\!\u3130-\u318f\uac00-\ud7a3]+','',s) 
def nfilter(s): 
	return re.sub(u'[^\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s) 

kkma = Kkma() 
req1 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7010929-Reviews-Balaji_Restaurant-Daegu.html') 
soup1 = BeautifulSoup(req1.text, 'html.parser') 
trip_name = [] 
trip_address = [] 
trip_menu = [] 
trip_point = [] 
name = soup1.find_all("h1") 
trip_name.append(name[1].get_text()) 
address = soup1.find("span", "_2saB_OSe").get_text() 
trip_address.append(address) 
menu = soup1.find("div", "_1XLfiSsv").get_text() 
trip_menu.append(menu) 
point = soup1.find("span", "r2Cf69qf").get_text() 
trip_point.append(hfilter(point)) 
req2 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7943036-Reviews-Hi_Thai-Daegu.html') 
soup2 = BeautifulSoup(req2.text, 'html.parser') 
name = soup2.find_all("h1") 
trip_name.append(name[1].get_text()) 
address = soup2.find("span", "_2saB_OSe").get_text() 
trip_address.append(address) 
menu = soup2.find("div", "_1XLfiSsv").get_text() 
trip_menu.append(menu) 
point = soup2.find("span", "r2Cf69qf").get_text() 
trip_point.append(hfilter(point)) 
req3 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d10218361-Reviews-Deira_Restaurant-Daegu.html') 
soup3 = BeautifulSoup(req3.text, 'html.parser') 
name = soup3.find_all("h1") 
trip_name.append(name[1].get_text()) 
address = soup3.find("span", "_2saB_OSe").get_text() 
trip_address.append(address) 
menu = soup3.find_all("a", "_2mn01bsa") 
trip_menu.append(menu[1].get_text()) 
point = soup3.find("span", "r2Cf69qf").get_text() 
trip_point.append(hfilter(point)) 
req4 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d7265417-Reviews-New_Saladdin-Daegu.html') 
soup4 = BeautifulSoup(req4.text, 'html.parser') 
name = soup4.find_all("h1") 
trip_name.append(name[1].get_text()) 
address = soup4.find("span", "_2saB_OSe").get_text() 
trip_address.append(address) 
menu = soup4.find("div", "_1XLfiSsv").get_text() 
trip_menu.append(menu) 
point = soup4.find("span", "r2Cf69qf").get_text() 
trip_point.append(hfilter(point)) 
req5 = requests.get('https://www.tripadvisor.co.kr/Restaurant_Review-g297886-d8055192-Reviews-Jungang_Tteokbokki-Daegu.html') 
soup5 = BeautifulSoup(req5.text, 'html.parser') 
name = soup5.find_all("h1") 
trip_name.append(name[1].get_text()) 
address = soup5.find("span", "_2saB_OSe").get_text() 
trip_address.append(address) 
menu = soup5.find("div", "_1XLfiSsv").get_text() 
trip_menu.append(menu) 
point = soup5.find("span", "r2Cf69qf").get_text() 
trip_point.append(hfilter(point)) 
#####################
#####################


###menupanCrawling###
#####################
def hfilter(s):
	return re.sub(u'[^\ \-\,\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def nfilter(s):
	return re.sub(u'[^\,\.\d\!\u3130-\u318f\uac00-\ud7a3]+','',s)
def kgwfilter(s):
	return re.sub(u'[^\d\ \-\|\u3130-\u318f\uac00-\ud7a3]+','',s)

name = []
score = []
location = []
category = []
req1 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=R700334')
soup1 = BeautifulSoup(req1.content, 'html.parser')
html_name1 = soup1.find(class_ = 'storeName')
html_score1 = soup1.find(class_ = 'total')
html_location1 = soup1.find(class_ = 'add1')
html_category1 = soup1.find(class_ = 'type')
name.append(hfilter(str(html_name1)).strip())
score.append(nfilter(str(html_score1)))
location.append(hfilter(str(html_location1)).strip()[10:])
category.append(hfilter(str(html_category1)).strip())
req2 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702258')
soup2 = BeautifulSoup(req2.content, 'html.parser')
html_name2 = soup2.find(class_ = 'storeName')
html_score2 = soup2.find(class_ = 'total')
html_location2 = soup2.find(class_ = 'add1') 
html_category2 = soup2.find(class_ = 'type') 
name.append(hfilter(str(html_name2)).strip())
score.append(nfilter(str(html_score2)))
location.append(hfilter(str(html_location2)).strip()[10:])
category.append(hfilter(str(html_category2)).strip())
req3 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702257')
soup3 = BeautifulSoup(req3.content, 'html.parser')
html_name3 = soup3.find(class_ = 'storeName')
html_score3 = soup3.find(class_ = 'total')
html_location3 = soup3.find(class_ = 'add1') 
html_category3 = soup3.find(class_ = 'type') 
name.append(hfilter(str(html_name3)).strip())
score.append(nfilter(str(html_score3)))
location.append(hfilter(str(html_location3)).strip()[10:])
category.append(hfilter(str(html_category3)).strip())
req4 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702247')
soup4 = BeautifulSoup(req4.content, 'html.parser')
html_name4 = soup4.find(class_ = 'storeName')
html_score4 = soup4.find(class_ = 'total')
html_location4 = soup4.find(class_ = 'add1') 
html_category4 = soup4.find(class_ = 'type') 
name.append(hfilter(str(html_name4)).strip())
score.append(nfilter(str(html_score4)))
location.append(hfilter(str(html_location4)).strip()[10:])
category.append(hfilter(str(html_category4)).strip())	
req5 = requests.get('https://www.menupan.com/Restaurant/Onepage.asp?acode=H702251')
soup5 = BeautifulSoup(req5.content, 'html.parser')
html_name5 = soup5.find(class_ = 'storeName')
html_score5 = soup5.find(class_ = 'total')
html_location5 = soup5.find(class_ = 'add1') 
html_category5 = soup5.find(class_ = 'type') 
name.append(hfilter(str(html_name5)).strip())
score.append(nfilter(str(html_score5)))
location.append(hfilter(str(html_location5)).strip()[10:])
category.append(hfilter(str(html_category5)).strip())
#####################
#####################
#######################Crawling END############################################
###############################################################################



#######################Elastic search START####################################
###############################################################################
es = Elasticsearch([{'host':es_host, 'port':es_port}],timeout=30)
for i in range(0,5):
	e1={
		"site":"siksin",
		"name":siksin_name[i].encode('utf-8'),
		"category":siksin_category[i].encode('utf-8'),
		"score":siksin_score[i].encode('utf-8'),
		"location":siksin_location[i].encode('utf-8'),
	}
	res = es.index(index='siksin', doc_type='sik', id = i, body =e1)
for i in range(0,5):
	e2={
		"site":"trip",
		"name":trip_name[i].encode('utf-8'),
		"category":trip_menu[i].encode('utf-8'),
		"score":trip_point[i].encode('utf-8'),
		"location":trip_address[i].encode('utf-8'),

	}
	res = es.index(index='trip', doc_type='tri', id = i, body =e2)
for i in range(0,5):
	e={
		"site":"d_code",
		"name":d_code[i].encode('utf-8'),
		"category":d_menu[i].encode('utf-8'),
		"score":d_point[i].encode('utf-8'),
		"location":d_address[i].encode('utf-8'),

	}
	res = es.index(index='d_code', doc_type='code', id = i, body =e)
for i in range(0,5):
	e={
		"site":"menupan",
		"name":name[i].encode('utf-8'),
		"category":category[i].encode('utf-8'),
		"score":score[i].encode('utf-8'),
		"location":location[i].encode('utf-8'),

	}
	res = es.index(index='menupan', doc_type='pan', id = i, body =e)
query1 = {"query":{"bool":{"must":[{"match":{"site":"siksin"}}]}}}
query2 = {"query":{"bool":{"must":[{"match":{"site":"trip"}}]}}}
query3 = {"query":{"bool":{"must":[{"match":{"site":"d_code"}}]}}}
query4 = {"query":{"bool":{"must":[{"match":{"site":"menupan"}}]}}}
lst1 =[]
lst2 =[]
lst3 = []
lst4 = []
while True:
	try:
		docs = es.search(index='siksin', body=query1, size=5)
		break
	except Exception as e:
		print('error')
		continue
if docs['hits']['total']['value']>0:	
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		lst1.append(tmp)
while True:
	try:
		docs = es.search(index='trip', body=query2, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		lst2.append(tmp)
while True:
	try:
		docs = es.search(index='d_code', body=query3, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		lst3.append(tmp)
while True:
	try:
		docs = es.search(index='menupan', body=query4, size=5)
		break
	except Exception as e:
		print(1)
		continue
if docs['hits']['total']['value']>0:
	for doc in docs['hits']['hits']:
		tmp = list(doc['_source'].values())
		lst4.append(tmp)

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
	
		return render_template('info.html', name=myname,siksin_location=siksin_location,d_address=d_address,trip_address=trip_address,location=location,lst1=lst1,lst2=lst2,lst3=lst3,lst4=lst4,)




if __name__=="__main__":
	app.run(debug=True)
	app.run(host="127.0.0.1", port="5000", debug=True)

