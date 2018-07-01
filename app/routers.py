from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
	posts = [
	    {
	        'author' : {'username': 'Silva'},
	        'body': 'hay wo you boy?!))'
	    }
	    ]
	return render_template('index.html', title = 'Home', posts = posts)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))	
			
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect('login')
		login_user(user, remember=form.remember_me.data)
		next_url = request.args.get("next")
		if not next_url or url_parse(next_url).netloc != '':
			next_url = url_for("index")
		return redirect(next_url)
	return render_template('login.html', title='Sign In', form=form)
	
@app.route('/reg', methods=['GET', 'POST'])
def reg():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Registrstion is gud')
		return redirect(url_for('login'))
	return render_template('register.html', form=form, title='Registr')