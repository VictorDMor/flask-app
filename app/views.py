#encoding:utf-8

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
# def index():
# 	user = {'nickname' : 'Victor'}
# 	posts = [
# 		{
# 			'author': {'nickname': 'Felipe'},
# 			'body': 'O trabalho no McDonalds esta muito bom!'
# 		},
# 		{
# 			'author': {'nickname': 'Pedro'},
# 			'body': 'Respeitem minha historia nas brigas de rua!'
# 		},
# 		{
# 			'author': {'nickname': 'Matheus Martins'},
# 			'body': 'Alguem disse anime?'
# 		}
# 	]

# 	return render_template('index.html', user=user, title='Vapo', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])	