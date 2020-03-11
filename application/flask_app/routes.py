from flask import render_template, request, redirect
from flask_app.forms import RegistrationForm, LoginForm, SearchForm
from flask_app import app
from flask_app.team_data import team


##################################################
#             MAIN DIRECTORY PAGES               #
##################################################
# NOTE: Defines Main directories page routes

#@app.route("/") # this will be moved to the actual home page later, but needs to be here for now
@app.route("/about") 
def about():
    return render_template('about.html', team=team) # team list is getting passed to about page

@app.route("/admin")
# @login_required # this decorator will be implimented later
def admin():
    return render_template('admin.html') 

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/', methods=['GET', 'POST']) # this is only here for M2, will be moved later
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    results = []
    if request.method == 'POST':
        results = ['test', 'test', 'test'] # for test obviously, jeez
        redirect('/search', code=302)
        return render_template("search.html", form=form, data=results)
    return render_template("search.html", form=form, data=[])

##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    return render_template("/about_team_member.html", team_member=team[0])

@app.route("/akhil")
def akhil():
    return render_template("/about_team_member.html", team_member=team[1])

@app.route("/chris")
def chris():
    return render_template("/about_team_member.html", team_member=team[2])

@app.route("/elliot")
def elliot():
    return render_template("/about_team_member.html", team_member=team[3])

@app.route("/thomas")
def thomas():
    return render_template("/about_team_member.html", team_member=team[4])

@app.route("/bakulia")
def bakulia():
    return render_template("/about_team_member.html", team_member=team[5])