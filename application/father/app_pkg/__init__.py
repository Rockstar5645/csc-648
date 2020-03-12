from flask import Flask
from flask import render_template, request
from father.app_pkg.forms import SearchForm
from father.database_manager.db_manager import DB


app = Flask(__name__)
# create DB object
db = DB()

@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    # assign form
    form = SearchForm()
    # determin HTTP method
    if request.method == 'POST':
        # query db
        results = db.search_like(form['category'], form['term'])
        return render_template('search.html', form=form, results=results)
    return render_template('search.html', form=form)
