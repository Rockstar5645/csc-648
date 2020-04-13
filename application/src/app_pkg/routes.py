from src.app_pkg.forms import SearchForm, LoginForm, RegistrationForm
from flask import render_template, request, redirect, url_for, make_response
from src.app_pkg import app
from src.app_pkg import db
from src.app_pkg.forms import RegistrationForm
from src.app_pkg.forms import SubmissionForm

################################################
#                GENERAL ROUTING               #
################################################
# Routing by accessible web pages, main routes

@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    # assign form and results list
    form = SearchForm()
    results = []
    # if : user submits POST request
    if request.method == 'POST':
        # query db
        term = request.form['term']
        cat = request.form['category']
        results = db.search(term, cat)
        form.category.default = cat
        form.term.default = term
        form.process()
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results)
    # else : GET fresh html page
    return render_template('search.html', form=form, results=results)

@app.route("/about") 
def about():
    form = SearchForm()
    team = db.get_team()
    return render_template('about.html', team=team, form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        result = {}
        isloggedin = make_response("isloggedin")
        result = db.login(request.form['username'], request.form['password'], '127.0.0.1')
        if result['status'] == 'success':
            isloggedin.set_cookie("isloggedin", True, maxAge=None)
            return redirect(url_for('search'), isloggedin=isloggedin)
        else:
            isloggedin.set_cookie("isloggedin", False, maxAge=None)
            return render_template('login.html', form=form, isloggedin=isloggedin)
    else:
        return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        result = {}
        result = db.register(request.form['username'], request.form['password'], request.form['first_name'], request.form['last_name'], request.form['phone_number'], request.form['email'])
        print(result)
        if result['status'] == 'success':
            return redirect(url_for('search'))
        else:
            return render_template('registration.html', form=form)
    else:
        return render_template('registration.html', form=form)

################################################
#                SINGLE MEDIA VIEW             #
################################################
@app.route('/single_media_view', methods=['GET', 'POST'])
def single_media_view():
    media_view = SubmissionForm()
    return render_template('single_media_view.html', media_view=media_view)

################################################
#                USER PROFILE                  #
################################################

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

################################################
#                Admin PROFILE                 #
################################################

@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')




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


