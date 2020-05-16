from flask import redirect, url_for, request
from src.app_pkg.routes.common import validate_helper
from src.app_pkg import app, db
from src.app_pkg.forms import MessageForm
from src.app_pkg.objects.user import User

@app.route('/send_message', methods=['POST'])
def send_message():
    user = User(request.cookies)
    subject = request.form['message-subject']
    message = request.form['message-text']
    media_id = request.form['media-id']
    db.send_message(user.session_token, media_id, subject, message)
    return redirect(url_for('search'))



