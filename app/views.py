#encoding:utf-8

from flask import render_template
from app import app

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