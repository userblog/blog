from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	remember_me = BooleanField("Запомнить меня")
	submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	email = StringField('Электронная почта', validators=[DataRequired(), Email()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Зарегистрироваться')
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Этот логин уже занят')
			
	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email is not None:
			raise ValidationError('Этот email уже занят')

class EditProfileForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
	submit = SubmitField('Сохранить')
    
    #Proverka imeni pro redaktorovanii profilya,
    #esli imya uge sushestvuet, to vydaetsa predupregdenie"""
    
	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError('Этот логин уже занят')
				
class PostForm(FlaskForm):
	post = TextAreaField('Ваша запись', validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField('Отправить')
	
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    submit = SubmitField('Сбросить пароль')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сохранить')
