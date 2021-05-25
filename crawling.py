#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

if __name__== '__main__':
	url = u'https://'
	res = requests.get(url)

	html = BeautifulSoup(res.content, "html.parser")

