from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3.dbapi2 import Cursor



app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
	message = 'Введите ваш логин и пароль.'
	username = ''
	password = ''
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

	if username == 'mkreep' and password == 'root':
		return redirect('/mainpage', code=302)
	else:
		message = 'Введите ваш логин и пароль.'
	return render_template('index.html', message=message)

@app.route('/mainpage')
def mainpage():
	#member_NickName = 
	return render_template('main.html')

if __name__ == '__main__':
	app.run()