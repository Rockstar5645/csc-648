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
# NOTE: This function handles the route for the file upload functionality.
# it provides user input data from the file upload button and gives it to the database digital_media API
# it also adds the files to the static folders and generates a thumbnail image of the original image

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# This function allows us to check for allowed file extensions for filenames
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# This is the main route that handles the file upload, thumbnail generation, and passing the data to the database
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

            # makes thumbnail and saves it to thumbnails folder
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

            
            license_val = request.form['license_field']
            price = 0.0
            if license_val == "2":
                try:
                    price = float(request.form['price'])

                except:
                    print("error: price is not a number")
                    return redirect(url_for('search'))

            cat = request.form['category']
            media = request.form['media_type']
            filepath = 'user_images/' + filename
            thumbpath = 'thumbnails/t_' + filename

            #print(name, " ", desc, " ", price, " ", cat, " ", media, " ", filepath, " ", thumbpath, " ", session_token)\

            db.upload_file(user.user_id, name, desc, filepath, thumbpath, cat, media, price, session_token)
            submission_form.filename.default = filename
            submission_form.description.default = desc
            submission_form.price.default = price
            submission_form.category.default = cat
            submission_form.media_type.default = media
            submission_form.process()

            return redirect(url_for('search'))

    # else, (if "GET")
    return render_template('search.html', search_form=search_form, submission_form=submission_form, user=user)

# this function returns the static path variable from config.py and appends the user_images folder and filename to the path
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['STATIC_PATH'] + 'user_images/', filename)