from app import app
from flask import render_template,redirect
from .models import Questionnaire,Question


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/healthtests")
def healthtests():
    healthtests = Questionnaire.query.all()
    return render_template("test.html",healthtests=healthtests)

@app.route("/healthtests/<int:naire_id>")
def healthtest(naire_id):
    questions = Question.query.filter_by(questionnaire_id=naire_id).all()
    return render_template("question.html",questions = questions)

@app.route("/api/submit")
def submit():
    return render_template("success.html")

@app.route("/healthcard")
def healthcard():
    return render_template("data.html")