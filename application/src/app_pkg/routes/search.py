from src.app_pkg.forms import SearchForm
from flask import render_template, request, make_response
from src.app_pkg import app, db
from src.app_pkg.routes.common import validate_helper

################################################
#                SEARCH / HOME                 #
################################################
# AUTHOR: Chris Eckhardt
# NOTE: This function handles the route of the searchbar functionality.
# it provides user input data from the search form and gives it to the database search API
# Once the Database manager API returns a result (as a list), it passes that resulting list
# to the HTML page to be rendered.

@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    isloggedin = validate_helper(request.cookies)
    form = SearchForm()
    results = []
    result_size = 0
    if request.method == 'POST':
        params = request.form
        result_size, results = call_db(params)
        set_form_defaults(form, params)
        return render_template('search.html', form=form, results=results, isloggedin=isloggedin, result_size=result_size)
    return render_template('search.html', form=form, isloggedin=isloggedin, result_size=result_size)


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

def call_db(params):
    print("search parameters: {}".format(str(params)))
    print('calling db...')
    result_size, result_list = db.search(params)
    print('search result size: {}'.format(str(result_size)))
    print('search result: {}'.format(str(result_list)))
    return result_size, result_list