from src.app_pkg.routes.common import validate_helper
from src.app_pkg import app, db
from src.app_pkg.forms import LoginForm
from flask import render_template, request, redirect, url_for, make_response
from src.app_pkg.objects.user import User

################################################
#                     LOGIN                    #
################################################

@app.route("/login", methods=['GET', 'POST'])
def login():
    user = User(request.cookies['token'])
    form = LoginForm()

    if request.method == 'POST':
        result = {}
        result = db.login(request.form['username'], request.form['password'], request.remote_addr)
        if result['status'] == 'success':
            print('login success')
            res = make_response(redirect(url_for('search')))
            res.set_cookie('token', result['token'])
            return res
        else:
            print('login fail')
            res = make_response(redirect(url_for('login')))
            res.set_cookie('token', 'none')
            return res
    else:
        return render_template('login.html', form=form, user=user)