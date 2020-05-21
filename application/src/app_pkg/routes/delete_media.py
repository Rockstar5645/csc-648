import os
from src.app_pkg import app, db
from flask import render_template, request, redirect, url_for
from src.app_pkg.objects.user import User

##################################################
#                DELETE MEDIA                    #
##################################################
# not tested yet
@app.route('/delete/<int:media_id>', methods=['GET', 'POST'])
def delete_media(media_id):
    user = User(request.cookies)
    try:
        media_path = db.get_digital_media_path_by_id(media_id)
        thumb_path = db.get_digital_media_thumbnail_path_by_id(media_id)
        abspath = str(os.getcwd())+'/src/app_pkg/static/'
        os.remove(abspath+media_path)
        os.remove(abspath+thumb_path)
        db.delete_file(media_id)
    except:
        print("an exception occurred in delete_media.py")
    return redirect('user_profile')