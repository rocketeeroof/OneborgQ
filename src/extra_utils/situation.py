from extra_utils.controller import controller
from extra_utils.render import scheduled_render

class situation():
    def __init__(self, renderer):
        self.packet = None
        self.own_index = 0
        self.own_team = 0
        self.field_info = None
        self.memory = None
        self.controller = None
        self.render = None
        self.ball_prediction = None
        self.reset_memory(renderer)

    def reset_memory(self, renderer):
        '''
        Reset long-term information.
        '''
        self.controller = controller()
        self.memory = memory()
        self.render = scheduled_render(renderer)

    def update(self, packet, field_info, ball_prediction, index, team):
        '''
        Reset short-term information.
        '''
        self.ball_prediction = ball_prediction
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