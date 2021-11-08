from flask import Flask, render_template, request
from datetime import datetime

webapp = Flask(__name__)

authors = []

@webapp.route("/")
def index():
    namen = "Hans"
    print(request.args)
    return render_template("index.html", namen=namen, datum_today=datetime.now(), p=request.args.get("p"))

@webapp.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        author = request.form.get("author")
        authors.append(author)

    return render_template("about.html", authors=authors)

@webapp.route("/contact", methods=["POST"])
def contact():

    user_name = request.form.get("user_name")
    password = request.form.get("password")

    print(user_name)
    print(password)

    return render_template("success.html", user=user_name, pw=password)

@webapp.route("/projects")
def project():
    projects= ["Flask Projects", "Boogle", "Fakebook"]
    return render_template("Project.html", projects = projects)

if __name__ == "__main__":
    webapp.run()