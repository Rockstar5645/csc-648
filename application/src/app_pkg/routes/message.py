from flask import render_template, request
from src.app_pkg.routes.common import validate_helper
from src.app_pkg import app, db
from src.app_pkg.forms import MessageForm

@app.route('/send_message', method=['GET', 'POST'])
def message():
    isloggedin = validate_helper(request.cookies)
    form = MessageForm()
    if request.method == 'POST':
        pass
        # get message data
        # call db
        # return to parent url (if this is a modal)


