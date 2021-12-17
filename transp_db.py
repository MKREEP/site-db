from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask import Flask, render_template, request
import sqlite3
from sqlite3.dbapi2 import Cursor

#...
@app.route('/index/', methods=['post', 'get'])
def index():	
	message = ''
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

	if username == 'mkreep' and password == 'pass':
		message = 'norm tema'
	else:
		message = 'huipi'

	return render_template('index.html', message=message)
#...
app.run()