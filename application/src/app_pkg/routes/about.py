from src.app_pkg.routes.common import validate_helper
from src.app_pkg import db, app
from flask import render_template, request
from src.app_pkg.forms import SearchForm
from src.app_pkg.forms import SubmissionForm
from src.app_pkg.objects.user import User


################################################
#                   ABOUT                      #
################################################

@app.route("/about",methods=['GET', 'POST'])
def about():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team = db.get_team()
    return render_template('about.html', team=team, search_form=search_form, submission_form=submission_form, user=user)


##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team_member = db.get_team("Avery")
    return render_template("about_team_member.html", team_member=team_member, search_form=search_form, submission_form=submission_form, user=user)

@app.route("/akhil")
def akhil():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team_member = db.get_team("Akhil")
    return render_template("about_team_member.html", team_member=team_member, search_form=search_form, submission_form=submission_form, user=user)

@app.route("/chris")
def chris():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team_member = db.get_team("Chris")
    return render_template("about_team_member.html", team_member=team_member, search_form=search_form, submission_form=submission_form, user=user)

@app.route("/elliot")
def elliot():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team_member = db.get_team("Elliot")
    return render_template("about_team_member.html", team_member=team_member, search_form=search_form, submission_form=submission_form, user=user)

@app.route("/thomas")
def thomas():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team_member = db.get_team("Thomas")
    return render_template("about_team_member.html", team_member=team_member, search_form=search_form, submission_form=submission_form, user=user)

@app.route("/bakulia")
def bakulia():
    user = User(request.cookies['token'])
    search_form = SearchForm()
    submission_form = SubmissionForm()
    team_member = db.get_team("Bakulia")
    return render_template("about_team_member.html", team_member=team_member, search_form=search_form, submission_form=submission_form, user=user)