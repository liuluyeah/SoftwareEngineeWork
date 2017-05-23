from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
basedir = os.path.abspath(".")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir,"questions.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Questionnaire(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    namespace = db.Column(db.String(60))
    description = db.Column(db.Text)
    questions = db.relationship("Question",backref='questionnaire',
                                lazy="dynamic")
    def __init__(self,namespace,description):
        self.namespace = namespace
        self.description = description

    def __repr__(self):
        return("<Questionnaire {}>".format(self.namespace))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("questionnaire.id"))
    answers = db.relationship("Answer", backref="question")
    def __init__(self,content,questionnaire_id):
        self.content = content
        self.questionnaire_id = questionnaire_id

    def __repr__(self):
        return("<Question {} belongto {}>".format(self.content,
                                                  self.questionnaire_id))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    def __init__(self,content,question_id):
        self.content = content
        self.question_id = question_id

    def __repr__(self):
        return("<Answer {} belong to {}>".format(self.content,
                                                 self.question_id))

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


if __name__ == "__main__":
    app.run()
