# from flask import render_template, request, make_response, jsonify
# from src.app_pkg.routes.common import validate_helper
# from src.app_pkg import app, db
# from src.app_pkg.forms import MessageForm
#
# ################################################
# #      Show All Messages / User Profile        #
# ################################################
# # AUTHOR: Bakulia Kurmant
# # NOTE: This function handles the route of the show all message functionality.
# # It show the list of messages the user sent or received and single view message modal with message body
# # Once the Database manager API returns a result (as a list), it passes that resulting list
# # to the HTML page to be rendered.
#
#
# @app.route('/user_profile', method=['GET'])
# def all_messages(msg_id):
#     isloggedin = validate_helper(request.cookies.get('token'))
#
#     if not isloggedin:
#         return render_template('search.html')
#
#     msg_result_size = 0
#     msg_results = []
#     print('calling db...')
#     msg_result_size, msg_results = db.get_all_messages(isloggedin, msg_id)
#
#     if msg_result_size == 0:
#         print("You have no messages!")
#
#     return render_template('user_profile.html', isloggedin=isloggedin, msg_result_size=msg_result_size,
#                            msg_results=msg_results)
#

