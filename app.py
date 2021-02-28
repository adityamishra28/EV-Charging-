from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aditya@localhost:5432/evcharging'
db = SQLAlchemy(app)

class charging(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    voltage = db.Column(db.Integer)
    battery_rate = db.Column(db.Integer)
    temperature = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/', methods = ['GET','POST'])
def index():
        tasks = charging.ordered_by.all()
        return render_template('update.html' , tasks = tasks)





