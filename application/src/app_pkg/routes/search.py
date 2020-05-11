from src.app_pkg.forms import SearchForm
from flask import render_template, request, make_response
from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper
from flask_paginate import Pagination, get_page_args

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

    def set_results(self, results):
        self.results = results

    def get_page(self, page=0):
        if len(self.results) == 0:
            print('TODO : fill empty list in results object, /routes/search.py')
        return self.results[page : page+12]

    def get_number_of_pages(self):
        return int(len(self.results)/12)

r = Results()

@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search(page=0):
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    if request.method == 'POST':
        params = request.form
        r.set_results( db.search(params) )
        set_form_defaults(form, params)
        return render_template('search.html', form=form, page=page, results=r.get_page(0), isloggedin=isloggedin, total_pages=r.get_number_of_pages())
    return render_template('search.html', form=form, isloggedin=isloggedin, results=r.get_page(page), total_pages=r.get_number_of_pages(), page=page)

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
