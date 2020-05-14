from src.app_pkg.routes.common import validate_helper
from src.app_pkg import app, db
from src.app_pkg.forms import RegistrationForm
from flask import render_template, request, make_response, redirect, url_for
from src.app_pkg.objects.user import User



################################################
#                REGISTER                      #
################################################

@app.route("/register", methods=['GET', 'POST'])
def register():
    user = User(request.cookies)
    form = RegistrationForm()

    if request.method == 'POST':
        result = {}
        email = request.form['email_prefix'] + request.form['email_suffix']
        result = db.register(request.form['username'], email,  request.form['password'])
        if result['status'] == 'success':
            if result['status'] == 'success':
                res = make_response(redirect(url_for('search')))
                res.set_cookie('token', result['token'], max_age=None)
                return res
            else:
                res = make_response(redirect(url_for('login')))
                res.set_cookie('token', 'none', max_age=None)
                return res
        else:
            return render_template('registration.html', form=form)
    else:
        return render_template('registration.html', form=form)
