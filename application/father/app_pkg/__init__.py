from flask import Flask
from flask import render_template, request
from father.app_pkg.team_data import team
from father.app_pkg.forms import SearchForm
from father.database_manager.db_manager import DB

# init flask application
app = Flask(__name__)
# create DB object
db = DB()

################################################
#                GENERAL ROUTING               #
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
        results = db.search(request.form['term'], request.form['category'])
        # return results -------------------------------------vvv
        return render_template('search.html', form=form, results=results)
    # else : GET fresh html page
    return render_template('search.html', form=form)

@app.route("/about") 
def about():
    return render_template('about.html', team=team) # team list is getting passed to about page



##################################################
#                TEAM MEMBER PAGES               #
##################################################
# NOTE: Defines team member "about" page routes

@app.route("/avery")
def avery():
    return render_template("/about_team_member.html", team_member=team[0])

@app.route("/akhil")
def akhil():
    return render_template("/about_team_member.html", team_member=team[1])

@app.route("/chris")
def chris():
    return render_template("/about_team_member.html", team_member=team[2])

@app.route("/elliot")
def elliot():
    return render_template("/about_team_member.html", team_member=team[3])

@app.route("/thomas")
def thomas():
    return render_template("/about_team_member.html", team_member=team[4])

@app.route("/bakulia")
def bakulia():
    return render_template("/about_team_member.html", team_member=team[5])