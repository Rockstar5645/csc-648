import os
from PIL import Image as PILImage
from tkinter import Image
from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from src.app_pkg.forms import SubmissionForm
from src.app_pkg.forms import SearchForm
from flask import render_template, request, redirect, url_for, make_response, flash, send_from_directory
from werkzeug.utils import secure_filename
from src.app_pkg.objects.user import User

##################################################
#                DELETE MEDIA                    #
##################################################

@app.route('/delete', methods=['GET', 'POST'])
def delete_file():
    user = User(request.cookies)

    file = request.form['']     # get file path or file name
    os.remove(file)             # remove file from static folder
    db.delete_file()            # delete file from db, pass args to function

    return render_template()