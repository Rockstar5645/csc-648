from src.app_pkg.forms import SearchForm
from src.app_pkg.forms import SubmissionForm
from flask import render_template, request, make_response
from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask_paginate import Pagination, get_page_args
from src.app_pkg.objects.user import User
import math

################################################
#                SEARCH / HOME                 #
################################################
# AUTHOR: Chris Eckhardt
# NOTE: This function handles the route of the searchbar functionality.
# it provides user input data from the search form and gives it to the database search API
# Once the Database manager API returns a result (as a list), it passes that resulting list
# to the HTML page to be rendered.

class Results(object):
    
    def __init__(self):
        self.results = []
        self.page = 1

    def set_results(self, results):
        self.results = results

    def get_page(self, page):
        if len(self.results) == 0:
            print('TODO : fill empty list in results object, /routes/search.py')
        offset = (page-1)*12
        return self.results[offset : offset+12]

    def get_number_of_pages(self):
        return math.ceil(len(self.results)/12)

    def set_page(self, page):
        if page >= 1 and page <= self.get_number_of_pages():
            self.page = page


r = Results()

@app.route('/', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/search', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search(page):
    user = User(request.cookies)
    search_form = SearchForm()
    submission_form = SubmissionForm()
    r.set_page(page)
    if request.method == 'POST':
        params = request.form
        r.set_results( db.search(params) )
        set_form_defaults(search_form, params)
        return render_template('search.html', search_form=search_form, submission_form=submission_form, page=r.page, results=r.get_page(1), user=user, total_pages=r.get_number_of_pages())
    return render_template('search.html', search_form=search_form, submission_form=submission_form, user=user, results=r.get_page(r.page), total_pages=r.get_number_of_pages(), page=r.page)

def set_form_defaults(form, params):
    form.category.default = params['category']
    form.term.default = params['term']
    form.license.default = params['license']
    if 'image_check' in params:
        form.image_check.default = params['image_check']
    if 'video_check' in params:
        form.video_check.default = params['video_check']
    if 'audio_check' in params:
        form.audio_check.default = params['audio_check']
    if 'document_check' in params:
        form.document_check.default = params['document_check']
    form.process()
