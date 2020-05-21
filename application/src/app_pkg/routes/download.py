from src.app_pkg import app, db
from flask import send_file, request
import os


##################################################
#                  DOWNLOAD                      #
##################################################
# Author: Chris Eckhardt
# This route takes the digital_media_id as a parameter, 
# looks up the file_path from the db, 
# then serves the file to the clients browser.

@app.route('/download/<int:media_id>', methods=['GET'])
def download_media(media_id):
    path = db.get_digital_media_path_by_id(media_id)
    print(app.config['UPLOAD_FOLDER'] + path)
    return send_file(app.config['UPLOAD_FOLDER'] + path, as_attachment=True)