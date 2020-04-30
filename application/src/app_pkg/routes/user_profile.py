from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request

################################################
#                USER PROFILE                  #
################################################

@app.route('/user_profile')
def user_profile():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    return render_template('user_profile.html', form=form, isloggedin=isloggedin)
