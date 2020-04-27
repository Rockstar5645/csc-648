import os
from tkinter import Image
from PIL import Image
from src.app_pkg.forms import SearchForm, LoginForm, RegistrationForm
from flask import render_template, request, redirect, url_for, make_response, flash, send_from_directory
from src.app_pkg import app
from src.app_pkg import db
from flask_login import login_required
from src.app_pkg.forms import RegistrationForm
from src.app_pkg.forms import SubmissionForm
from werkzeug.utils import secure_filename
from src.config import STATIC_PATH

################################################
#                GENERAL ROUTING               #
################################################
# Routing by accessible web pages, main routes

################################################
#                SEARCH / HOME                 #
################################################

@app.route('/', methods=['GET', 'POST'], defaults={'page':1})
@app.route('/search', defaults={'page':0}, methods=['GET', 'POST'])
@app.route('/search/page/<int:page>', methods=['GET','POST'])
def search(page):
    isloggedin = validate_helper(request.cookies)
    # assign form and results list
    form = SearchForm()
    perpage = 12
    print('page: '.format(request.args.get('page')))
    startat=page*perpage
    # if : user submits POST request
    if request.method == 'POST':
        # get form data
        results = []
        term = request.form['term']
        cat = request.form['category']
        # query db, handle results and pagination
        results = db.search(term, cat, startat, perpage)
        # set form persistance
        form.category.default = cat
        form.term.default = term
        form.process()
        # set pagination navigation
        if page == 3:
            next_url = 0
        else:
            next_url = page+1
        if page == 0:
            prev_url = 3
        else:
            prev_url = prev_url-1
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results, isloggedin=isloggedin, next_url=next_url, prev_url=prev_url, page=page)
    # else : GET fresh html page
    return render_template('search.html', form=form, isloggedin=isloggedin, page=0)

################################################
#                     LOGIN                    #
################################################

@app.route("/login", methods=['GET', 'POST'])
def login():
    isloggedin = validate_helper(request.cookies)
    form = LoginForm()
    if request.method == 'POST':
        result = {}
        result = db.login(request.form['username'], request.form['password'], request.remote_addr)
        if result['status'] == 'success':
            print('login success')
            res = make_response(redirect(url_for('search')))
            res.set_cookie('token', result['token'])
            return res
        else:
            print('login fail')
            res = make_response(redirect(url_for('login')))
            res.set_cookie('token', 'none')
            return res
    else:
        return render_template('login.html', form=form)

################################################
#                REGISTER                      #
################################################

@app.route("/register", methods=['GET', 'POST'])
def register():
    isloggedin = validate_helper(request.cookies)
    form = RegistrationForm()
    if request.method == 'POST':
        result = {}
        result = db.register(request.form['username'], request.form['email'],  request.form['password'])
        if result['status'] == 'success':
            if result['status'] == 'success':
                res = make_response(redirect(url_for('search')))
                res.set_cookie('token', result['token'], max_age=None)
                return res
            else:
                res = make_response(redirect(url_for('login')))
                res.set_cookie('token', 'none', max_age=None)
                return res
        else:
            return render_template('registration.html', form=form)
    else:
        return render_template('registration.html', form=form)

################################################
#                   ABOUT                      #
################################################

@app.route("/about",methods=['GET', 'POST']) 
def about():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team = db.get_team()
    return render_template('about.html', team=team, form=form, isloggedin=isloggedin)

################################################
#                SINGLE MEDIA VIEW             #
################################################
@app.route('/single_media_view', methods=['GET', 'POST'])
def single_media_view():
    isloggedin = validate_helper(request.cookies.get('token'))
    media_view = SubmissionForm()
    return render_template('single_media_view.html', media_view=media_view, isloggedin=isloggedin)

################################################
#                USER PROFILE                  #
################################################

@app.route('/user_profile')
def user_profile():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    return render_template('user_profile.html', form=form, isloggedin=isloggedin)

################################################
#                Admin PROFILE                 #
################################################

@app.route('/admin_page')
#@login_required
def admin_page():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    return render_template('admin_page.html', form=form, isloggedin=isloggedin)

##################################################
#                SUBMIT MEDIA                    #
##################################################
# work in progress
# thumbnail saved in thumbnails folder works, added STATIC_PATH = /User/.../static/ in config.py to test
# replace ... with your path in your local setup
app.config['STATIC_PATH'] = STATIC_PATH
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
            file.save(os.path.join(STATIC_PATH + 'user_images/', filename))

            # makes thumbnail and saves it to thumbnails folder
            f = Image.open(STATIC_PATH + 'user_images/' + filename)
            f.thumbnail((200, 200))
            f.save(STATIC_PATH + 'thumbnails/t_' + filename)
            print("thumbnail saved")

            name = request.form['filename']
            desc = request.form['description']
            price = request.form['price']
            cat = request.form['category']
            filepath = 'user_images/' + filename
            thumbpath = 'thumbnails/t_' + filename
            owner_id = 1

            print(name, " ", desc, " ", price, " ", cat, " ", filepath, " ", thumbpath)

            # query db params, approval variable and session token not implemented yet
            results = []
            results = db.upload(name, desc, filepath, thumbpath, cat, price)
            print(results)

            form.filename.default = filename
            form.description.default = desc
            form.price.default = price
            form.category.default = cat
            form.process()
            # TODO: fix render_templates and redirects for submit media button in base.html
            return redirect(url_for('search'))

    # else, (if "GET")
    return render_template('upload.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['STATIC_PATH'] + 'user_images/', filename)


##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team_member = db.get_team("Avery")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/akhil")
def akhil():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team_member = db.get_team("Akhil")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/chris")
def chris():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team_member = db.get_team("Chris")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/elliot")
def elliot():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team_member = db.get_team("Elliot")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/thomas")
def thomas():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team_member = db.get_team("Thomas")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

@app.route("/bakulia")
def bakulia():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    team_member = db.get_team("Bakulia")
    return render_template("about_team_member.html", team_member=team_member, form=form, isloggedin=isloggedin)

##################################################
#             HELPER FUNCTIONS                   #
##################################################

def clear_cookies():
        res = make_response(redirect(url_for('home')))
        res.set_cookie('token', 'invalid')
        return res

def validate_helper(cookies):
    if 'token' in cookies:
        v_message = db.validate_session(cookies['token'])
        if (v_message['status'] == 'success'):
            return True
    return False

def delete_file(path):
    os.remove(path)
    print('FILE DELETED : {}'.format(path))
