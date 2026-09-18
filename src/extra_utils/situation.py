from extra_utils.controller import controller

class situation():
    def __init__(self):
        self.packet = None
        self.own_index = 0
        self.field_info = None
        self.memory = None
        self.controller = None
        self.render = None
        self.reset_memory()

    def reset_memory(self):
        self.memory = memory()
        self.controller = controller()

    def update(self, packet, field_info, index, team):
        self.controller = controller()
        self.packet = packet
        self.own_index = index
        self.own_team = team
        self.field_info = field_info

class memory():
    def __init__(self):
        self.last_tick = last_tick()
        self.context = None

class last_tick():
    def __init__(self):
        self.x = 0

class context():
    def __init__(self):
        self.active_sequence = None