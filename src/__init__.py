# Import Third-Party
from bottle import Bottle, Route


# Import Home-Grown
from src.controllers import CONTROLLERS


class Backend(Bottle):
    
    controllers = {}

    def __init__(self):
        super().__init__()

        self.init_controllers()
    

    def add_route(self, abs_path, http_method, callback):
        route = Route(self, abs_path, http_method, callback)
        super().add_route(route)



    def init_controllers(self):
        for controller_cls in CONTROLLERS:
            self._init_controller(controller_cls)



    def _init_controller(self, controller_cls):
        ctrl = controller_cls(self)
         
        self.controllers[ctrl.instance_name]  = ctrl

        path_base, routes = ctrl.make_routes()
        for http_method, rel_path, callback in routes:
            abs_path = f'{path_base}/{rel_path}'
            self.add_route(abs_path, http_method, callback)



