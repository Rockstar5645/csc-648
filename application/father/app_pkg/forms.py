from father.app_pkg import db
from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


################################################
#                    FORMS                     #
################################################
class SearchForm(Form):
    term = StringField("Search", validators=[], default='')
    categories = db.get_category_select_field()
    category = SelectField(u'Category', choices=categories, validators=[], default='all')
    submit = SubmitField("Search")

class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')