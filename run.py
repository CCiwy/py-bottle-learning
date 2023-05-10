#!/usr/bin/env python
#-*- encode: utf-8 -*-
from src import Backend
from bottle import run

app = Backend()





run(app, host='localhost', port=8080, reloader=True)
