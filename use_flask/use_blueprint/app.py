#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask import Flask, url_for, render_template

from login import logining

from admin import admin

app = Flask(__name__, static_url_path="", root_path="")

app.register_blueprint(logining, url_prefix='/login')

app.register_blueprint(admin, url_prefix='/admin')


@app.route('/')
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port=8000, debug=True)
