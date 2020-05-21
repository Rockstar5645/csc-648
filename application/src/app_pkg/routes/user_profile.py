from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask import render_template, request
from src.app_pkg.forms import SearchForm, SubmissionForm
from src.app_pkg.objects.user import User
import math

################################################
#                USER PROFILE                  #
################################################
# On dashboard the user shall be able to see the following:
# digital media title as a button for single view media modal,
# media type, category, datetime, price, status, delete button.

class Page(object):
    
    def __init__(self):
        self.messages = []
        self.items = []
        self.messages_page = 1
        self.items_page = 1

    def set_lists(self, messages, items):
        self.messages = messages
        self.items = items

    def get_message_page(self, page):
        if len(self.messages) == 0:
            return
        offset = (self.messages_page-1)*12
        return self.messages[offset : offset+12]

    def get_items_page(self, page):
        if len(self.items) == 0:
            return
        offset = (self.items_page-1)*12
        return self.items[offset : offset+12]

    def get_number_of_message_pages(self):
        return math.ceil(len(self.messages)/12)

    def get_number_of_item_pages(self):
        return math.ceil(len(self.items)/12)

    def set_message_page(self, page):
        if page >= 1 and page <= self.get_number_of_message_pages():
            self.message_page = page

    def set_item_page(self, page):
        if page >= 1 and page <= self.get_number_of_item_pages():
            self.items_page = page

p = Page()


@app.route('/user_profile', methods=['GET', 'POST'], defaults={'m_page': 1, 'i_page': 1})
def user_profile(m_page, i_page):
    user = User(request.cookies)
    search_form = SearchForm()
    submission_form = SubmissionForm()

    p.set_item_page(i_page)
    p.set_message_page(m_page)
    
    # Get user digital media
    p.items = user.get_digital_media()

    # Get user messages
    t_messages = user.get_messages()

    if t_messages['status'] == 'success': 
        p.messages = t_messages['message-list']
    else:
        p.messages=[]

    return render_template('user_profile.html', 
    search_form=search_form, submission_form=submission_form, 
    user=user, messages=p.messages, digital_media=p.items, 
    messages_page=p.messages_page, item_page=p.items_page,
    total_message_pages = p.get_number_of_message_pages(),
    total_item_pages = p.get_number_of_item_pages())



