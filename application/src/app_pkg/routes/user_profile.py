from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request
from src.app_pkg.forms import SearchForm
from src.app_pkg.forms import SubmissionForm

################################################
#                USER PROFILE                  #
################################################

@app.route('/user_profile')
def user_profile():
    isloggedin = validate_helper(request.cookies)
    search_form = SearchForm()
    submission_form = SubmissionForm()
    return render_template('user_profile.html', search_form=search_form, submission_form=submission_form, isloggedin=isloggedin)
