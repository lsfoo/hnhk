from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.password = password


    def __repr__(self):
        return '<User %r>' % self.username
