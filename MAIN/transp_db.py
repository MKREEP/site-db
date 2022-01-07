# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3.dbapi2 import Cursor





application = Flask(__name__)
app = Flask(__name__)
@application.route('/', methods=['POST', 'GET'])
def index():
	username = ''
	password = ''
	if request.method == 'POST':
		username = str(request.form.get('username'))
		password = str(request.form.get('password'))

		conn = sqlite3.connect('ProjectMembers.db')
		cur = conn.cursor()
		print('БД подключена к SQLite успешно.')
		
		result_login = str(cur.execute('SELECT login FROM logins_passwords WHERE login=?;', (username,)).fetchone()[0])
		result_password = str(cur.execute('SELECT password FROM logins_passwords WHERE login=?;', (username,)).fetchone()[0])
		if password == result_password:
			return redirect('mainpage')
		else:
			return redirect('error_login')

	return render_template('index.html')

	# else:
	# 	message = 'Введите ваш логин и пароль.'
	# return render_template('index.html', message=message)

@application.route('/mainpage')
def mainpage():
	#member_NickName = 
	return render_template('main.html')

@application.errorhandler(500)
def error_login(e):
	return render_template('error500.html')

@application.route('/error_login')
def login_error():
	return render_template('login_error.html')

if __name__ == '__main__':
	application.run(host='0.0.0.0')
