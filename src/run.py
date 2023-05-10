#!/usr/bin/env python
#-*- encode: utf-8 -*-


# Import Third-Party
from bottle import run
from bottle import Bottle


app = Bottle()


@app.route('/index')
def index():
    return '<h1>INDEX</h1>'


@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'



run(app, host='localhost', port=8080, reloader=True)
