from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask import Flask
import sqlite3
from sqlite3.dbapi2 import Cursor


class contactForm(object):
	name = StringField('Name: ', validators=[DataRequired()])
	submit = SubmitField('Submit')


