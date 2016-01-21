#encoding: utf-8

from app import db
from flask.ext.login import LoginManager
lm = LoginManager()

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	pw = db.Column(db.String(64), index=True, unique=True)
	authenticated = db.Column(db.Boolean, index=True, unique=True)

	def is_active(self):
		return True

	def get_id(self):
		''' Retorna o e-mail do usuario '''
		return self.email

	def is_authenticated(self):
		''' True se o usuário estiver autenticado '''
		return self.authenticated

	def __repr__(self):
		return '<User %r>' % (self.nickname)

	@lm.user_loader
	def user_loader(user_id):
		''' Dado o id do usuário, retornar o objeto Usuário correspondente '''
		return User.query.get(user_id)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % (self.body)