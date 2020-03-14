from flask import Flask
from flask import render_template, request
from father.app_pkg.forms import SearchForm
from father.database_manager.db_manager import DB

# init flask application
app = Flask(__name__)
# create DB object
db = DB()

################################################
#                   ROUTING                    #
################################################
@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    # assign form and results list
    form = SearchForm()
    results = []
    # if : user submits POST request
    if request.method == 'POST':
        # query db
        results = db.search_like(request.form['category'], request.form['term'])
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results)
    # else : GET fresh html page
    return render_template('search.html', form=form)
