from flask import Flask, render_template
app = Flask(__name__)

team = [ # list of team members and path to their page
    {
        'name': 'Bakulia',
        'link': '/bakulia'
    },
    {
        'name': 'Akhil',
        'link': '/akhil'
    },
    {
        'name': 'Chris',
        'link': '/chris'
    },
    {
        'name': 'Elliot',
        'link': '/elliot'
    },
    {
        'name': 'Thomas',
        'link': '/thomas'
    },
    {
        'name': 'Avery',
        'link': '/avery'
    }
]

#### ABOUT APPLICATION ###
@app.route("/") # this will be moved to the actual home page later, but needs to be here for now
@app.route("/about") 
def about():
    return render_template('about.html', team=team) # team list is getting passed to about page

@app.route("/bakulia")
def bakulia():
    return render_template("/team/bakulia.html")

@app.route("/akhil")
def akhil():
    return render_template("/team/akhil.html")

@app.route("/chris")
def chris():
    return render_template("/team/chris.html")

@app.route("/elliot")
def elliot():
    return render_template("/team/elliot.html")

@app.route("/thomas")
def thomas():
    return render_template("/team/thomas.html")

@app.route("/avery")
def avery():
    return render_template("/team/avery.html")




### run flask application ###
if __name__ == "__main__":
    app.run()