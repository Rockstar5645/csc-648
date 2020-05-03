import os
from src.app_pkg import db
from flask import request, make_response, redirect, url_for



##################################################
#             HELPER FUNCTIONS                   #
##################################################

def clear_cookies():
        res = make_response(redirect(url_for('home')))
        res.set_cookie('token', 'invalid')
        return res

def validate_helper(cookies):
    if 'token' in cookies:
        v_message = db.validate_session(cookies['token'])
        if (v_message['status'] == 'success'):
            return True
    return False

def delete_file(path):
    os.remove(path)
    print('FILE DELETED : {}'.format(path))