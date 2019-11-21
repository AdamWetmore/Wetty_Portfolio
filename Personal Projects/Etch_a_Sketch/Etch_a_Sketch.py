import turtle


class Etch_a_sketch:
    def __init__(self):
        self.t = turtle.Turtle()
        self.screen = self.t.getscreen()
        self.t.speed(0)
        self.screen.delay(0)
        self.screen.onkeypress(self.move_right,'Right')
        self.screen.onkeypress(self.move_up,'Up')
        self.screen.onkeypress(self.move_left,'Left')
        self.screen.onkeypress(self.move_down,'Down')
        self.screen.listen()
    def move_right(self):
        self.t.seth(0)
        self.t.fd(5)
    def move_up(self):
        self.t.seth(90)
        self.t.fd(5)
    def move_left(self):
        self.t.seth(180)
        self.t.fd(5)
    def move_down(self):
        self.t.seth(270)
        self.t.fd(5)


Etch_a_sketch()
