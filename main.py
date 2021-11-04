from flask import Flask, render_template

webapp = Flask(__name__)

@webapp.route("/")
def index():
    return render_template("index.html")

@webapp.route("/about")
def about():
    return render_template("about.html")

@webapp.route("/projects")
def project():
    return render_template("Project.html")

if __name__ == "__main__":
    webapp.run()