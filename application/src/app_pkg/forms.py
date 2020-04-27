##############################################
#   Flask Forms
#
#   These will be used in all front end form input
#
###############################################

from src.app_pkg import db
from flask_wtf import RecaptchaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


################################################
#                    FORMS                     #
################################################
class SearchForm(Form):
    term = StringField("Search", validators=[], default='')
    categories = db.get_category_select_field()
    category = SelectField('Category', choices=categories, validators=[])
    category = SelectField('Category', choices=categories, validators=[], default='all')
    submit = SubmitField("Search")

class RegistrationForm(Form):
    first_name = StringField("First Name", validators=[ Length(min=2, max=20)])
    last_name = StringField("Last Name", validators=[ Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    username = StringField("Username", validators=[])
    password = PasswordField('Password', validators=[])
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

class SubmissionForm(Form):
    filename = StringField('File Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    categories = db.get_category_select_field()
    category = SelectField('Category', choices=categories, validators=[])
    category = SelectField('Category', choices=categories, validators=[], default='all')
    submit = SubmitField('Submit Media')

