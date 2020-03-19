from flask import Flask
from flask import render_template, request
from father.app_pkg.team_data import team
from father.database_manager.db_manager import DB
from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# init flask application
app = Flask(__name__)
# create DB object
db = DB()


################################################
#                    FORMS                     #
################################################
class SearchForm(Form):
    term = StringField("Search", validators=[])
    categories = db.get_category_select_field()
    category = SelectField(u'Category', choices=categories, validators=[])
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

################################################
#                GENERAL ROUTING               #
################################################
@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    # assign form and results list
    form = SearchForm()
    results = []
    # if : user submits POST request
    if request.method == 'POST':
        # query db
        results = db.search(request.form['term'], request.form['category'])
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results)
    # else : GET fresh html page
    return render_template('search.html', form=form)

@app.route("/about") 
def about():
    return render_template('about.html', team=team) # team list is getting passed to about page



##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    return render_template("/about_team_member.html", team_member=db.get_team("Avery"))

@app.route("/akhil")
def akhil():
    return render_template("/about_team_member.html", team_member=db.get_team("Akhil"))

@app.route("/chris")
def chris():
    return render_template("/about_team_member.html", team_member=db.get_team("Chris"))

@app.route("/elliot")
def elliot():
    return render_template("/about_team_member.html", team_member=db.get_team("Elliot"))

@app.route("/thomas")
def thomas():
    return render_template("/about_team_member.html", team_member=db.get_team("Thomas"))

@app.route("/bakulia")
def bakulia():
    return render_template("/about_team_member.html", team_member=db.get_team("Bakulia"))