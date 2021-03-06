from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskforum.models import User
class RegistrationForm(FlaskForm):
     username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
     email=StringField('Email',validators=[DataRequired(),Email()])
     password=PasswordField('Password',validators=[DataRequired()])
     confirm_password=PasswordField('Conform Password',validators=[DataRequired(),EqualTo('password')])
     submit=SubmitField('Sign up')
     def validate_username(self,username):
          user=User.query.filter_by(username=username.data).first()
          if user:
               raise ValidationError('That name is already taken please use a different come')
     def validate_email(self,email):
          user=User.query.filter_by(email=email.data).first()
          if user:
               raise ValidationError('That emailID is already taken please use a different come')

class LoginForm(FlaskForm):
     email=StringField('Email',validators=[DataRequired(),Email()])
     password=PasswordField('Password',validators=[DataRequired()])
     remember=BooleanField('Remember me')
     submit=SubmitField('Log in')