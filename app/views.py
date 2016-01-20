#encoding:utf-8

from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, models
from flask.ext.wtf import Form
from .forms import LoginForm
from models import User
from flask.ext.login import LoginManager
lm = LoginManager()

def load_user(id):
	return User.query.get(int(id))

posts = []
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	user = {'nickname': 'Victor'}
	if len(request.args) != 0:
		posts.append({
	 		'author': {'nickname': request.args['name']},
			'body': request.args['post']
		})
		return render_template('index.html', title='Novo post adicionado!', user=user, posts=posts)
	else:
		return render_template('index.html', title='Novo post adicionado!', user=user, posts=posts)

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
	if form.validate_on_submit():
		user = User.query.get(form.email.data)
		if user:
			if bcrypt.check_password_hash(user.pw, form.pword.data):
				user.authenticated = True
				db.session.add(user)
				db.session.commit()
				login_user(user, remember=True)
				return redirect(url_for('index'))
 	return render_template('login.html', title='Login de usuario')
 		

