from extra_utils.controller import controller

class scheduled_render():
    def __init__(self, renderer):
        self.renderer = renderer
        self.renders = []

    def reset(self):
        '''
        Clear the render objects used.
        '''
        self.renders = []

    def add_line(self, p1, p2, col):
        self.renders.append(rendered_line(p1, p2, col))

    def add_string(self, txt, p, s, col):
        self.renders.append(rendered_string(txt, p, s, col))

    def render_all(self):
        '''
        Render everything at once.
        '''
        for i in self.renders:
            i.render(self.renderer)

class rendered_line():
    def __init__(self, p1, p2, col):
        self.p1 = p1
        self.p2 = p2
        self.col = col

    def render(self, renderer):
        renderer.draw_line_3d(
            self.p1, self.p2, self.col
        )

class rendered_string():
    def __init__(self, txt, p, s, col):
        self.txt = txt
        self.p = p
        self.s = s
        self.col = col

    def render(self, renderer):
        renderer.draw_string_3d(
            self.txt, self.p, self.s, self.col
        )