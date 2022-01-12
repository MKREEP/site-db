# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3.dbapi2 import Cursor




application = Flask(__name__)

@application.route('/')
def mainpage():
	return render_template('mainpage.html')

@application.route('/login', methods=['POST', 'GET'])
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
			return redirect('home')
		else:
			return redirect('error_login')

	return render_template('index.html')

@application.route('/home')
def personal_page():
	return render_template('personal.html')

@application.errorhandler(500)
def error_login(e):
	return render_template('error500.html')

@application.route('/error_login')
def login_error():
	return render_template('login_error.html')

@application.route('/registration', methods=['POST', 'GET'])
def reg():
	member_NickName = ''
	member_DiscordTag = ''
	member_EMail = ''
	member_Discord = ''
	member_Login = ''
	member_Password = ''

	if request.method == 'POST':
		member_NickName = str(request.form.get('member_NickName'))
		member_DiscordTag = str(request.form.get('member_DiscordTag'))
		member_EMail = str(request.form.get('member_eMail'))
		member_Discord = str(request.form.get('member_Discord'))
		member_Login = str(request.form.get('member_Login'))
		member_Password = str(request.form.get('member_Password'))

		conn = sqlite3.connect('ProjectMembers.db')
		cur = conn.cursor()
		print('БД подключена к SQLite успешно.')

		loginCheck = str(cur.execute('SELECT login FROM logins_passwords WHERE login=?;', (member_Login,)).fetchone()[0])
		if loginCheck == member_Login:
			pass

		member_RegData = (member_NickName, member_DiscordTag, member_EMail, member_Discord)
		cur.execute("INSERT INTO members(NickName, DiscordTag, Email, Discord) VALUES(?, ?, ?, ?);", member_RegData)
		conn.commit()

		login_RegData = (member_Login, member_Password)
		cur.execute("INSERT INTO logins_passwords(login, password) VALUES(?, ?);", login_RegData)
		conn.commit()

	return render_template('reg_page.html')

if __name__ == '__main__':
	application.run(host='0.0.0.0')
