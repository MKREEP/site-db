from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from sqlite3.dbapi2 import Cursor



app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
	message = ''
	username = ''
	password = ''
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

	if username == 'mkreep' and password == 'root':
		message = 'ok, lets go!'
		return redirect(url_for('/main'))
	else:
		message = 'Неверный логин или пароль.'
	return render_template('index.html', message=message)

@app.route('/main')
def main():
	bd = 23
	return render_template('main.html')

if __name__ == '__main__':
	app.run()