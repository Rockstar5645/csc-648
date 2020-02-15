from flask import Flask, render_template, url_for
app = Flask(__name__)

##################################################
#                    TEAM LIST                   #
##################################################
# NOTE: list of team members and associated data, 
# this will later be removed when team data is moved to DB
# ...or not, doesnt really matter

team = [

    {
        'name': 'Avery Chen',
        'link': '/avery',
        'position': 'position',
        'image': 'static/images/test_image.jpeg',
        'description': 'description here'
    },
    {
        'name': 'Akhil Gandu',
        'link': '/akhil',
        'position': 'GitHub Master',
        'image': 'static/images/akhil.jpg',
        'description': 'Master of GitHub'
    },
    {
        'name': 'Chris Eckhardt',
        'link': '/chris',
        'position': 'position',
        'image': 'static/images/chris.jpeg',
        'description': 'description here'
    },
    {
        'name': 'Elliot Yardley',
        'link': '/elliot',
        'position': 'Front-End Lead',
        'image': 'static/images/elliot.jpg',
        'description': 'description here'
    },
    {
        'name': 'Thomas Yu',
        'link': '/thomas',
        'position': 'position',
        'image': 'static/images/test_image.jpeg',
        'description': 'description here'
    },
    {
        'name': 'Bakulia Kurmant',
        'link': '/bakulia',
        'position': 'position',
        'image': 'static/images/bakulia.jpeg',
        'description': 'description here'
    }

]

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
# NOTE: This instantiates and runs the flask application

if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run()
