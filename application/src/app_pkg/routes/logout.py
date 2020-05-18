from src.app_pkg.routes.common import validate_helper
from src.app_pkg import app, db
from flask import render_template, request, redirect, url_for, make_response
from src.app_pkg.objects.user import User

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    user = User(request.cookies)
    if user.isloggedin:
        db.logout(request.cookies['token'])
        return redirect(url_for('search'))
    else:
        return redirect(url_for('search'))
    