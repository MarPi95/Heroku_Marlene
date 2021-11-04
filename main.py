from flask import Flask, render_template
from datetime import datetime

webapp = Flask(__name__)

@webapp.route("/")
def index():
    namen = "Hans"
    return render_template("index.html", namen=namen, datum_today=datetime.now)

@webapp.route("/about")
def about():
    return render_template("about.html")

@webapp.route("/projects")
def project():
    projects= ["Flask Projects", "Boogle", "Fakebook"]
    return render_template("Project.html")

if __name__ == "__main__":
    webapp.run()