
from flask import render_template
from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from src.app_pkg.forms import SubmissionForm
from flask import render_template, request

################################################
#                SINGLE MEDIA VIEW             #
################################################
@app.route('/single_media_view', methods=['GET', 'POST'])
def single_media_view():
    isloggedin = validate_helper(request.cookies.get('token'))
    media_view = SubmissionForm()
    return render_template('single_media_view.html', media_view=media_view, isloggedin=isloggedin)