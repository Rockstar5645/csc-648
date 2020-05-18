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
#                SUBMIT MEDIA                    #
##################################################

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/submit', methods=['GET', 'POST'])
def upload_file():
    user = User(request.cookies)
    search_form = SearchForm()
    submission_form = SubmissionForm()

    # if "POST"
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            cwd = os.getcwd()
            newPath = cwd.replace(os.sep, '/')
            fullPath = os.path.join(newPath + '/', 'src/app_pkg/static/user_images/', filename)
            file.save(fullPath)
            user_images = os.path.join(newPath + '/', 'src/app_pkg/static/')

            #makes thumbnail and saves it to thumbnails folder
            f = PILImage.open(fullPath)
            f.thumbnail((200, 200))
            f.save(user_images + 'thumbnails/t_' + filename)
            print("thumbnail saved")

            # query db params, add approval variable
            session_token = request.cookies.get('token')
            name = request.form['filename']
            desc = request.form['description']


            license_val = request.form['license_field']
            print("Value", license_val)            
            price = request.form['price'] if license_val == "2" else 0.00          


            cat = request.form['category']
            media = request.form['media_type']
            filepath = 'user_images/' + filename
            thumbpath = 'thumbnails/t_' + filename

            print(name, " ", desc, " ", price, " ", cat, " ", media, " ", filepath, " ", thumbpath, " ", session_token)\

            db.upload_file(user.user_id, name, desc, filepath, thumbpath, cat, media, price, session_token)
            submission_form.filename.default = filename
            submission_form.description.default = desc
            submission_form.price.default = price
            submission_form.category.default = cat
            submission_form.media_type.default = media
            submission_form.process()

            return redirect(url_for('search'))

    # else, (if "GET")
    return render_template('search.html', search_form=search_form, submission_form=submission_form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['STATIC_PATH'] + 'user_images/', filename)