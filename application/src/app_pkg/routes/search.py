from src.app_pkg.forms import SearchForm
from flask import render_template, request, make_response
from src.app_pkg import app
from src.app_pkg import db
from src.app_pkg.routes.common import validate_helper

################################################
#                SEARCH / HOME                 #
################################################

@app.route('/', methods=['GET', 'POST'], defaults={'page':1})
@app.route('/search', defaults={'page':0}, methods=['GET', 'POST'])
@app.route('/search/page/<int:page>', methods=['GET','POST'])
def search(page):
    isloggedin = validate_helper(request.cookies)
    # assign form and results list
    form = SearchForm()
    perpage = 12
    startat=page*perpage
    # if : user submits POST request
    if request.method == 'POST':
        # get form data
        results = []
        term = request.form['term']
        cat = request.form['category']
        media_t = request.form['media_type']
        # query db, handle results and pagination
        results = db.search(term, cat, media_t, startat, perpage)
        # set form persistance
        form.category.default = cat
        form.term.default = term
        form.process()
        # set pagination navigation
        if page == 3:
            next_url = 0
        else:
            next_url = page+1
        if page == 0:
            prev_url = 3
        else:
            prev_url = prev_url-1
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results, isloggedin=isloggedin, next_url=next_url, prev_url=prev_url, page=page)
    # else : GET fresh html page
    return render_template('search.html', form=form, isloggedin=isloggedin, page=0)