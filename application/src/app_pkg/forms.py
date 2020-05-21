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
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField, IntegerField, SelectMultipleField, widgets, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange, Regexp

################################################
#                    FORMS                     #
################################################

class SearchForm(Form):
    categories = db.get_category_select_field()
    term = StringField("Search", validators=[Length(min=2, max=40)], default='')
    category = SelectField('Category', choices=categories, validators=[], default='all')
    image_check = BooleanField("image", validators=[], default=False)
    video_check = BooleanField("video", validators=[], default=False)
    audio_check = BooleanField("audio", validators=[], default=False)
    document_check = BooleanField("document", validators=[], default=False)
    license = SelectField('license', choices=[('all', 'all'), ('free', 'free'), ('paid', 'paid')], validators=[], default='all')
    submit = SubmitField("Search")

class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email_prefix = StringField("Email", validators=[DataRequired(), Length(min=2, max=30)])
    suffix = [('@sfsu.edu', '@sfsu.edu'), ('@mail.sfsu.edu','@mail.sfsu.edu')]
    email_suffix = SelectField('Category', choices=suffix, validators=[], default='@sfsu.edu')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    username = StringField("Username", validators=[])
    password = PasswordField('Password', validators=[])
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

class SubmissionForm(Form):
    filename = StringField('File Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    price = IntegerField('Price', validators=[Regexp('^[0-9]+$')])
    categories = db.get_category_select_field()
    categories.remove(('all', 'all'))
    categories.insert(0,('', 'Select'))
    media_types = db.get_media_type_select_field()
    media_types.remove(('all', 'all'))
    media_types.insert(0,('', 'Select'))
    licenses = [("1", "Free"), ("2", "Paid")]
    category = SelectField('Category', choices=categories, validators=[DataRequired()])
    media_type = SelectField('Media Type', choices=media_types, validators=[DataRequired()])
    license_field = SelectField('License', choices=licenses, validators=[])
    submit = SubmitField('Submit')
#
class MessageForm(Form):
    subject = StringField('subject line', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField('Submit')


