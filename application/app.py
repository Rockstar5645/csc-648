from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database.database_manager import Database_Manager
from config import Config
from tests.team_data import team
import os, sys


app = Flask(__name__)
app.config['AQLALCHEMY_DATABASE_URI'] = Config.database
db = SQLAlchemy(app)
database_manager = Database_Manager(db)


##################################################
#             MAIN DIRECTORY PAGES               #
##################################################
# NOTE: Defines Main directories page routes

@app.route("/") # this will be moved to the actual home page later, but needs to be here for now
@app.route("/about") 
def about():
    return render_template('about.html', team=team) # team list is getting passed to about page

@app.route("/admin")
# @login_required # this decorator will be implimented later
def admin():
    return render_template('admin.html') 

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

##################################################
#             RUN FLASK APPLICATION              #
##################################################
# NOTE: run flask server

if __name__ == "__main__":
    app.run(host='0.0.0.0')