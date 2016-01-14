#encoding:utf-8

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Victor'}
	posts = [
		{
			'author': {'nickname': 'Felipe'},
			'body': 'O trabalho no McDonalds esta muito bom!'
		},
		{
			'author': {'nickname': 'Pedro'},
			'body': 'Respeitem minha historia nas brigas de rua!'
		},
		{
			'author': {'nickname': 'Matheus Martins'},
			'body': 'Alguem disse anime?'
		}
	]

	return render_template('index.html', user=user, title='Vapo', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)	