#!/usr/bin/env python
#-*- encode: utf-8 -*-


# Import Third-Party
from bottle import run
from bottle import Bottle, Route


class Backend(Bottle):
    
    controllers = {}

    def add_route(self, abs_path, http_method, callback):

        route = Route(self, abs_path, http_method, callback)
        super().add_route(route)

    def init_controller(self, controller_cls):
        ctrl = controller_cls(self)
         
        self.controllers[ctrl.instance_name]  = ctrl

        path_base, routes = ctrl.make_routes()
        for http_method, rel_path, callback in routes:
            abs_path = f'{path_base}/{rel_path}'
            self.add_route(abs_path, http_method, callback)


class Controller:
    instance_name = 'test'

    def __init__(self, app):
        self.app = app

    def make_routes(self):
        path_base = '/test'
        routes = [
            ("GET", "index", self.index),
            ("GET", "second", self.second),
            ]
        return path_base, routes


    def index(self):
        return 'CONTROLLER INDEX'


    def second(self):
        return 'second route'



app = Backend()
app.init_controller(Controller)





run(app, host='localhost', port=8080, reloader=True)
