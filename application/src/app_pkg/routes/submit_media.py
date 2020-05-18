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

# CODE REVIEW: There is a title comment but no explanation of this files function, 
# The large submit function has inline comments and this is good.
# Overall, good job, only small details need to be changed.

##################################################
#                SUBMIT MEDIA                    #
##################################################

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# RECOMMENDED ACTION: add header with short description
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# RECOMMENEDED ACTION: add header with short description
@app.route('/submit', methods=['GET', 'POST'])
def upload_file():
    # RECOMMENEDED ACTION: we need to check this user object 
    # to make sure they are logged into a valid account before 
    # allowing them to upload files
    user = User(request.cookies)
    # CODE REVIEW: Forms have descriptive names, GOOD!
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

            # RECOMMENEDED ACTION: print statements should be left for diagnostic purposes only, 
            # if they are useful for debug and you wish to keep ityou should comment it out.
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

# RECOMMENEDED ACTION: add a short header comment with description of function
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['STATIC_PATH'] + 'user_images/', filename)