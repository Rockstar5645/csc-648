from flask import Flask
from flask import render_template
from app_pkg.forms import SearchForm



app = Flask(__name__)

@app.route('/')
@app.route('/search')
def search():
    form = SearchForm()
    return render_template('search.html', form=form)
