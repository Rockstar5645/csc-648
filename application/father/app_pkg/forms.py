from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SearchForm(Form):
    term = StringField("Search", validators=[])
    categories = [ ('all', 'all'), ('picture', 'picture'), ('video', 'video'), ('audio', 'audio'), ('documents', 'documents')]
    category = SelectField(u'Category', choices = categories, validators=[])
    submit = SubmitField("Search")