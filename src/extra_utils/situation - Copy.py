from extra_utils.controller import controller

class situation():
    def __init__(self):
        self.packet = None
        self.memory = None
        self.controller = None
        self.reset_memory()

    def reset_memory(self):
        self.memory = memory()
        self.controller = controller()

    def update(self, packet):
        self.controller = controller()
        self.packet = packet

class memory():
    def __init__(self):
        self.last_tick = None
        self.context = None

class last_tick():
    def __init__(self):
        self.x = 0