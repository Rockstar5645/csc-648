from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request
from src.app_pkg.forms import SearchForm

################################################
#                USER PROFILE                  #
################################################

@app.route('/user_profile')
def user_profile():
    isloggedin = validate_helper(request.cookies)
    # form = SearchForm()
    return render_template('user_profile.html',  isloggedin=isloggedin)
