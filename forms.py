from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=16)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Please Enter a Valid Email')])
    password = PasswordField('Password',validators=[DataRequired(),
                                                    Length(min=6, max=26)])
    verify_password = PasswordField('Verify Password', validators=[DataRequired(),
                                                                   Length(min=6, max=26), EqualTo('password')])
    submit = SubmitField('Signup')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Please Enter a Valid Email')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, max=26)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
