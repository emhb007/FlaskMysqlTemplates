from flask import render_template

from application import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Eoghan's Magic Show")

# use base template

@app.route("/welcome/<name>/")
def template_base(name):
    return render_template('base.html', name=name, group='Sky Cohort 4')