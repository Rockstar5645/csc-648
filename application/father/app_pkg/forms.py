from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SearchForm(Form):
    term = StringField("Search", validators=[DataRequired()])
    categories = [ ('all', 'all'), ('pictures', 'pictures'), ('videos', 'videos')]
    category = SelectField(u'Category', choices = categories, validators = [DataRequired()])
    submit = SubmitField("Search")