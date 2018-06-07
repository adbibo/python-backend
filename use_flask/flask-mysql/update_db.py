#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adbibo@localhost/flask'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    phone = db.Column(db.String(32), nullable=False)

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone


news = User.query.all()
print news
news[1].username = 'test'
db.session.commit()
