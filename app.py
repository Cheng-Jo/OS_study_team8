#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('home.html')
@app.route('/info', methods=['GET', 'POST'])
def info():
	error = None
	if request.method == 'POST':
		myname = request.form['rating']
		return render_template('info.html', name=myname)
	else:
		myname = request.args.get('rating')
		return render_template('info.html', name=myname)

if __name__=="__main__":
  app.run(debug=True)
  app.run(host="127.0.0.1", port="5000", debug=True)

