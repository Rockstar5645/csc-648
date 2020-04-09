from tkinter import Image
from src.app_pkg.forms import SearchForm
from flask import render_template, request, jsonify
from datetime import datetime

from src.app_pkg.forms import SearchForm, LoginForm, RegistrationForm, SubmissionForm
from flask import render_template, request, redirect, url_for
from src.app_pkg import app
from src.app_pkg import db

from src.app_pkg.forms import RegistrationForm
from src.app_pkg.forms import SubmissionForm



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
    team = db.get_team()
    return render_template('about.html', team=team)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('registration.html', form=form)

##################################################
#                SUBMIT MEDIA                    #
##################################################
# work in progress
@app.route("/submit", methods=["GET", "POST"])
def submit():
    try:
        form = SubmissionForm(request.form)
        # if "POST"
        if request.method == "POST" and form.validate():

            # query db params
            filename = request.form['filename']
            desc = request.form['description']
            price = request.form['price']
            cat = request.form['category']

            # TODO: move example file into static/user_images

            # TODO: make example thumbnail, will change paths and image files later
            # added "from tkinter import Image" at the top
            path = 'M2_test_images'
            im1 = '/example.jpg'
            f = Image.open(path + im1)
            f.thumbnail((200, 200))
            f.save('thumbnails/example_t.jpg')

            # TODO: add db query params
            results = db.submit_media()

            form.filename.default = filename
            form.description.default = desc
            form.price.default = price
            form.category.default = cat
            form.process()

            # TODO: fix render_templates and redirects, not sure what html pages to use
            return render_template('search.html', form=form)

        # else, (if "GET")
        return render_template('', form=form)

    except Exception as e:
        return str(e)

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


