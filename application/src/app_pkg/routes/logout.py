from src.app_pkg.routes.common import validate_helper
from src.app_pkg import app, db
from flask import render_template, request, redirect, url_for, make_response

@app.route("/login", methods=['GET', 'POST'])
def login():
    isloggedin = validate_helper(request.cookies)
    if isloggedin:
        db.logout(request.cookies['token'])
        return redirect(url_for('search'))
    