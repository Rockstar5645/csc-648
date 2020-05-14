from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request
from src.app_pkg.forms import SearchForm
from src.app_pkg.forms import SubmissionForm
from src.app_pkg.routes.search import Results

################################################
#                USER PROFILE                  #
################################################
# On dashboard the user shall be able to see the following:
# digital media title as a button for single view media modal,
# media type, category, datetime, price, status, delete button.



@app.route('/user_profile')
def user_profile():
    isloggedin = validate_helper(request.cookies.get('token'))
    search_form = SearchForm()
    submission_form = SubmissionForm()
    # user_data = []

    return render_template('user_profile.html', search_form=search_form, submission_form=submission_form, isloggedin=isloggedin)


