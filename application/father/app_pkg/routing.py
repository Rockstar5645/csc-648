from father.app_pkg.forms import SearchForm
from flask import render_template, request
from father.app_pkg import app
from father.app_pkg import db
from father.app_pkg.forms import RegistrationForm



################################################
#                GENERAL ROUTING               #
################################################
# Routing by accessable web pages, main routes 

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
        return render_template('search_result.html', form=form, results=results)
    # else : GET fresh html page
    return render_template('search.html', form=form)

@app.route("/about") 
def about():
    team = db.get_team()
    return render_template('about.html', team=team)


##################################################
#                REGISTER AND LOGIN             #
##################################################

#
# class RegistrationForm(Form):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')
#
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     try:
#         form = RegistrationForm(request.form)
#
#         if request.method == "POST" and form.validate():
#             username = forms.RegistrationForm.username.data
#             email = forms.RegistrationForm.email.data
#             password = forms.RegistrationForm.password.data
#
#         return render_template("registration.html", form=form)
#
#     except Exception as e:
#         return str(e)



##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    team_member = db.get_team("Avery")
    return render_template("about_team_member.html", team_member=team_member)

@app.route("/akhil")
def akhil():
    team_member = db.get_team("Akhil")
    return render_template("about_team_member.html", team_member=team_member)

@app.route("/chris")
def chris():
    team_member = db.get_team("Chris")
    return render_template("about_team_member.html", team_member=team_member)

@app.route("/elliot")
def elliot():
    team_member = db.get_team("Elliot")
    return render_template("about_team_member.html", team_member=team_member)

@app.route("/thomas")
def thomas():
    team_member = db.get_team("Thomas")
    return render_template("about_team_member.html", team_member=team_member)

@app.route("/bakulia")
def bakulia():
    team_member = db.get_team("Bakulia")
    return render_template("about_team_member.html", team_member=team_member)


