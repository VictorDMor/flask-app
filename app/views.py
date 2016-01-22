#encoding:utf-8

from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, models
from flask.ext.wtf import Form
from .forms import LoginForm
from models import User
import flask.ext.login as flask_login
from flask.ext.security import login_required
lm = flask_login.LoginManager()
lm.init_app(app)

@lm.user_loader
def user_loader(id):
	return User.query.get(id)


posts = []
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	if len(request.args) != 0:
		posts.append({
	 		'author': {'nickname': request.args['name']},
			'body': request.args['post']
		})
		return render_template('index.html', title='Novo post adicionado!', posts=posts)
	else:
		return render_template('index.html', title='Bem-vindo!', posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def sign():
	if len(request.form) != 0:
		u = models.User(nickname=request.form['nickname'], email=request.form['email'], pw=request.form['pword'], authenticated=False)
		db.session.add(u)
		db.session.commit()
		flash('Usuario cadastrado com sucesso!')
		return render_template('signup.html', title='Cadastro de usuario')
	else:
		return render_template('signup.html', title='Cadastro de usuario')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.email.data is not None and form.pword.data is not None:
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			if user.pw == form.pword.data:
				lm.login_view = 'login'
				user.authenticated = True
				db.session.add(user)
				db.session.commit()
				flask_login.login_user(user)
				flask_login.current_user = user
				return render_template('index.html', title='Usuario logado!')
			else:
				flash('Senha incorreta!')
				return render_template('login.html', title='Login de usuario')
	return render_template('login.html', title='Login de usuario')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	''' Faz logout do usuário '''
	user = flask_login.current_user
	if user.is_authenticated is False:
		return render_template('login.html', title='Voce precisa logar primeiro!')
	else:
		user.authenticated = False
		db.session.add(user)
		db.session.commit()
		flask_login.logout_user()
		db.session.expunge(user)
		return render_template('index.html', title='Logout feito com sucesso!')

 		

