from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request
from src.app_pkg.forms import SearchForm, SubmissionForm
from src.app_pkg.objects.user import User

################################################
#                USER PROFILE                  #
################################################
# On dashboard the user shall be able to see the following:
# digital media title as a button for single view media modal,
# media type, category, datetime, price, status, delete button.



@app.route('/user_profile')
def user_profile():
    user = User(request.cookies)
    search_form = SearchForm()
    submission_form = SubmissionForm()
    messages = user.get_messages()
    if messages['status'] == 'success': 
        messages = messages['message-list']
    else:
        messages=[]
    return render_template('user_profile.html', search_form=search_form, submission_form=submission_form, user=user, messages=messages)



