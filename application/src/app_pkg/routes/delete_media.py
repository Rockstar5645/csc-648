import os
from src.app_pkg import app, db
from flask import render_template, request, redirect, url_for
from src.app_pkg.objects.user import User

##################################################
#                DELETE MEDIA                    #
##################################################
# not tested yet
@app.route('/delete', methods=['GET', 'POST'])
def delete_file():
    user = User(request.cookies)
    media_id = request.form['media-id']
    media_path = user.get_digital_media_path_by_id(media_id)
    os.remove(media_path)
    db.delete_file(media_id)
    return redirect(url_for('search'))