from extra_utils.controller import controller

class scheduled_render():
    def __init__(self):
        self.renders = []

    def reset(self):
        self.renders = []