from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask import Flask, render_template, request
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
		return redirect('/main', code=302)
	else:
		message = 'not lets go(('
	return render_template('index.html', message=message)

if __name__ == '__main__':
	app.run()