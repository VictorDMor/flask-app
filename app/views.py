#encoding:utf-8

from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from .models import User
import pdb

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



