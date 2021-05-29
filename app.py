#!/usr/bin/python3

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/북문')
def index2():

	return render_template('북문.html')

@app.route('/쪽문')
def index3():
	return render_template('쪽문.html')

@app.route('/정문')
def index4():
	return render_template('정문.html')

@app.route('/테크노문')
def index5():
	return render_template('테크노문.html')

if __name__=="__main__":
  app.run(debug=True)
  app.run(host="127.0.0.1", port="5000", debug=True)
