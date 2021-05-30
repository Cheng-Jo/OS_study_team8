#!/usr/bin/python3
#-*- coding: utf-8 -*-

import argparse
import subprocess
from flask import Flask, jsonify
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('home.html')
<<<<<<< HEAD

@app.route('/east', methods=['POST'])
def east():
        error = None
        myString = request.form['name']
        list = myString.split()
        return render_template('north.html', info1=list[0], info2 = list[1], info3 = list[2], info4 = list[3], info5 = list[4])


@app.route('/west', methods=['POST'])
def west():
        error = None
        myString = request.form['name']
        list = myString.split()
        return render_template('north.html', info1=list[0], info2 = list[1], info3 = list[2], info4 = list[3], info5 = list[4])

@app.route('/south', methods=['POST'])
def south():
        error = None
        myString = request.form['name']
	list = myString.split()
        return render_template('north.html', info1=list[0], info2 = list[1], info3 = list[2], info4 = list[3], info5 = list[4])



@app.route('/north', methods=['POST'])
def north():
        error = None
	myString = request.form['name']
	list = myString.split()
        return render_template('north.html', info1=list[0], info2 = list[1], info3 = list[2], info4 = list[3], info5 = list[4])


=======
@app.route('/info', methods=['GET', 'POST'])
def info():
	error = None
	if request.method == 'POST':
		myname = request.form['rating']
		return render_template('info.html', name=myname)
	else:
		myname = request.args.get('rating')
		return render_template('info.html', name=myname)
>>>>>>> 727bd81910041a2405fe57eec7556e7ead1f10c5

if __name__=="__main__":
  app.run(debug=True)
  app.run(host="127.0.0.1", port="5000", debug=True)

