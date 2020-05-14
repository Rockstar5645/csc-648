from src.app_pkg import app, db
from src.app_pkg.forms import SearchForm
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request
from src.app_pkg.objects.user import User


################################################
#                Admin PROFILE                 #
################################################

@app.route('/admin_page')
#@login_required
def admin_page():
    user = User(request.cookies)
    form = SearchForm()
    return render_template('admin_page.html', form=form, user=user)
