

class TestController:

    instance_name = 'test'

    def __init__(self, app):
        self.app = app

    def make_routes(self):
        path_base = '/test'
        routes = [
            ("GET", "index", self.index),
            ("GET", "second", self.second)
            ]
        return path_base, routes


    def index(self):
        return 'CONTROLLER INDEX'


    def second(self):
        return 'second route'


CONTROLLERS = [TestController]
