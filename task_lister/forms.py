from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired,Email, EqualTo, ValidationError , Length
from task_lister.models import User
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message = "Invalid Email Address")])
    mobile = StringField('Mobile Number', validators= [DataRequired(), Length(min =10 , max = 10, message = "Mobile Number should be 10 digits")])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired() , EqualTo('password', message = "Passwords must Match!!")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use different Username.')

    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email is not None:
            return ValidationError('Please use a different email address.')

    def validate_mobile(self, mobile):
        mob = User.query.filter_by(mob = mobile.data).first()
        if mob is not None:
            return ValidationError('Please use a different Mobile Number.')        
    

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(message = "Username Required")])
    password = PasswordField('Password', validators = [DataRequired(message = "Password Required")])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    t_head = StringField('Task Heading', validators = [DataRequired(message = "Enter Task Heading!!")])
    t_body = StringField('Task Description')
    ddate = DateField('Deadline Date',format = '%Y-%m-%d', validators = [DataRequired(message = "Deadline Required!!")])
    submit = SubmitField('Add Task')

class ChangePass(FlaskForm):
    old_pass = PasswordField('Old Password',validators = [DataRequired(message = "Old Password is required!!!")])
    new_pass = PasswordField('New Password',validators = [DataRequired(message = "New Password is required!!!")])
    rep_new_pass = PasswordField('Repeat New Password', validators = [DataRequired(),EqualTo('new_pass',message = "Passwords must Match")])
    submit = SubmitField('Change Password')   