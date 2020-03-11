from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


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

class SearchForm(Form):
    term = StringField("Search", validators=[DataRequired()])
    categories = [ ('1', 'all'), ('2', 'pictures'), ('3', 'videos')]
    category = SelectField(u'Category', choices = categories, validators = [DataRequired()])
    submit = SubmitField("Search")

class NewDigitalMedia(Form):
    name = StringField('MediaName', validators=[DataRequired(), Length(min=2, max=20)])
    description = StringField('MediaDescription', validators=[DataRequired(), Length(max=150)])
    file = FileField('MediaFile')
    submit = SubmitField("Submit")
