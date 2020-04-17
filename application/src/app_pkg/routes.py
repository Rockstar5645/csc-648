import os
from tkinter import Image

from src.app_pkg.forms import SearchForm, LoginForm, RegistrationForm
from flask import render_template, request, redirect, url_for, make_response, flash, send_from_directory
from src.app_pkg import app
from src.app_pkg import db
from flask_login import login_required
from src.app_pkg.forms import RegistrationForm
from src.app_pkg.forms import SubmissionForm
from werkzeug.utils import secure_filename
# from src.config import UPLOAD_FOLDER

################################################
#                GENERAL ROUTING               #
################################################
# Routing by accessible web pages, main routes

################################################
#                SEARCH / HOME                 #
################################################


@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    isloggedin = request.cookies.get('isloggedin')
    # assign form and results list
    form = SearchForm()
    # if : user submits POST request
    if request.method == 'POST':
        # query db
        results = []
        term = request.form['term']
        cat = request.form['category']
        results = db.search(term, cat)
        form.category.default = cat
        form.term.default = term
        form.process()
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results, isloggedin=isloggedin)
    # else : GET fresh html page
    return render_template('search.html', form=form, isloggedin=isloggedin)

################################################
#                   ABOUT                      #
################################################

@app.route("/about",methods=['GET', 'POST']) 
def about():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team = db.get_team()
    return render_template('about.html', team=team, form=form, isloggedin=isloggedin)

################################################
#                     LOGIN                    #
################################################

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        result = {}
        result = db.login(request.form['username'], request.form['password'], '127.0.0.1')
        if result['status'] == 'success':
            resp = make_response(redirect(url_for('search')))
            resp.set_cookie("isloggedin", 'true')
            return resp
        else:
            resp = make_response(url_for('login'))
            resp.set_cookie("isloggedin", 'false')
            return resp
    else:
        return render_template('login.html', form=form)

################################################
#                REGISTER                      #
################################################

@app.route("/register", methods=['GET', 'POST'])
def register():
    isloggedin = request.cookies.get('isloggedin')
    form = RegistrationForm()
    if request.method == 'POST':
        result = {}
        result = db.register(request.form['username'], request.form['email'],  request.form['password'])
        print(result)
        if result['status'] == 'success':
            return redirect(url_for('login'))
        else:
            return render_template('registration.html', form=form, isloggedin=isloggedin)
    else:
        return render_template('registration.html', form=form, isloggedin=isloggedin)

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
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    return render_template('user_profile.html', form=form, isloggedin=isloggedin)

################################################
#                Admin PROFILE                 #
################################################

@app.route('/admin_page')
@login_required
def admin_page():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    return render_template('admin_page.html', form=form, isloggedin=isloggedin)

##################################################
#                SUBMIT MEDIA                    #
##################################################
# work in progress

# path for UPLOAD_FOLDER is in config.py
# UPLOAD_FOLDER = /Users.../user_images
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/submit', methods=['GET', 'POST'])
def upload_file():
    form = SubmissionForm()
    # if "POST"
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

        # query db params, approval variable and session token not implemented yet
        filename = request.form['filename']
        desc = request.form['description']
        price = request.form['price']
        cat = request.form['category']

        # make example thumbnail
        path = 'user_images'
        im1 = file
        f = Image.open(path + im1)
        f.thumbnail((200, 200))
        f.save('thumbnails/' + f)

        # TODO: add db query params, not tested yet
        results = db.submit_media(filename, desc, im1, f, price, cat)

        form.filename.default = filename
        form.description.default = desc
        form.price.default = price
        form.category.default = cat
        form.process()

    # TODO: fix render_templates and redirects for submit media button in base.html
    # else, (if "GET")
    return render_template('upload.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team_member = db.get_team("Avery")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/akhil")
def akhil():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team_member = db.get_team("Akhil")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/chris")
def chris():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team_member = db.get_team("Chris")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/elliot")
def elliot():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team_member = db.get_team("Elliot")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/thomas")
def thomas():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team_member = db.get_team("Thomas")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/bakulia")
def bakulia():
    isloggedin = request.cookies.get('isloggedin')
    form = SearchForm()
    team_member = db.get_team("Bakulia")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)
