from src.app_pkg import db
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
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')

class SubmissionForm(Form):
    # added FileRequired and FileAllowed for more functionality when uploading files
    # TODO: make validators more detailed, add any missing form data
    filename = StringField('File Name', validators=[DataRequired()])
    #file = FileField('File', validators=[FileRequired(), FileAllowed(['jpeg', 'png'])])
    description = StringField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    categories = db.get_category_select_field()
    # category = SelectField('Category', choices=categories, validators=[])
    category = SelectField('Category', choices=categories, validators=[], default='all')
    submit = SubmitField('Submit Media')

