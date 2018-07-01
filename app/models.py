from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
	
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	possword_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy=True)
	
	def set_password(self, password):
		generate_password_hash(self.password_hash)
		
	def check_password(srlf, password):
		return check_password_hash(self.password_hash, password)
		
	def __repr__(self):
		return '<User: {}>'.format(self.username)
	
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(256))
	timestamp = db.Column(db.DateTime(), default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Body: {}>'.format(self.body)
		