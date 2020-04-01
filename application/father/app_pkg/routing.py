from father.app_pkg.forms import SearchForm, LoginForm, RegistrationForm
from flask import render_template, request
from father.app_pkg import app
from father.app_pkg import db


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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # TODO: validators (forms)
    if request.method == 'POST':
        results = db.login(request.form['username'], request.form['password'], '0.0.0.0')
        # if success
            # redirect home page
        # else
            # redirect to login w/ error
        pass
    else:
        pass
        # render login page

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
     # TODO: validators (forms)
    if request.method == 'POST':
        pass
        # call register()
        # if result is success
            # redirect to homepage
        # else
            # redirect to register w/ error
    else:
        pass
        # render register

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