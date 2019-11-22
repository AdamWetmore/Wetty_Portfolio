
import random, turtle


def rand_color():
    return random.choice(["red", "orange", "yellow",
                          "green", "blue", "purple"])

class Shape:
    def __init__(self, x=0, y=0, color=''):
        self.x = x
        self.y = y
        self.color = color
    def set_color(self,st):
        self.color = st
    def get_color(self):
        return self.color
    def __str__(self):
        loc = "loc:("+str(self.x)+", "+str(self.y)+"), "
        col = "color:"+self.color
        return loc + col
    def draw(self,t):
        t.setpos(self.x,self.y)



class Circle(Shape):
    def __init__(self, x=0, y=0, rad=0):
        Shape.__init__(self,x,y,rand_color())
        self.rad = rad
    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + ", rad:"+str(self.rad)
    def draw(self,t):
        t.penup()
        t.setpos(self.x,self.y-self.rad)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.rad)
        t.end_fill()
    def is_in(self,x,y):
        if (((self.x - x) ** 2) + (self.y - y) ** 2) ** .5 <= self.rad:
            return True
        else:
            return False


    

class Rectangle(Shape):
    def __init__(self,x,y,width=20,height=20):
        Shape.__init__(self,x,y,rand_color())
        self.width = width
        self.height = height
    def __str__(self):
        loc_color = Shape.__str__(self)
        return loc_color + ', w:' + str(self.width) + ', h:' + str(self.height)
    def draw(self,t):
        t.penup()
        Shape.draw(self,t)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)
        t.end_fill()
    def is_in(self,x,y):
        x_min = self.x
        y_min = self.y
        x_max = self.x + self.width
        y_max = self.y + self.height
        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            return True
        else:
            return False



    
class Display:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t2 = turtle.Turtle()
        self.t2.shape('turtle')
        self.sc = self.t.getscreen()
        self.elements = []
        self.t.speed(0)
        self.sc.delay(0)
        self.t.ht()
        self.sc.onclick(self.mouse_event)
        self.sc.onkeypress(self.move_up,'Up')
        self.sc.onkeypress(self.move_right,'Right')
        self.sc.onkeypress(self.move_down,'Down')
        self.sc.onkeypress(self.move_left,'Left')
        self.sc.listen()
    def feast(self):
        for i in self.elements:
            if i.is_in(self.t2.xcor(),self.t2.ycor()) == True:
                self.remove(i)
                self.t2.color(i.color)
                self.t2.shapesize(self.t2.shapesize()[0]*1.2)
                self.t2.pensize(self.t2.pensize()*1.2)
    def mouse_event(self,x,y):
        Flag = False
        for i in self.elements:
            if i.is_in(x,y) == True:
                self.remove(i)
                Flag = True
        if not(Flag):
            shape = random.choice(['rect','circ'])
            if shape == 'circ':
                new_circ = Circle(x,y,random.randint(10,50))
                self.elements.append(new_circ)
                new_circ.draw(self.t)
            else:
                new_rect = Rectangle(x,y,random.randint(10,50),random.randint(10,50))
                self.elements.append(new_rect)
                new_rect.draw(self.t)
    def remove(self, target):
        self.elements.remove(target)
        self.t.clear()
        for i in self.elements:
            i.draw(self.t)
    def move_right(self):
        self.t2.seth(0)
        self.t2.forward(10)
        self.feast()
    def move_up(self):
        self.t2.seth(90)
        self.t2.forward(10)
        self.feast()
    def move_left(self):
        self.t2.seth(180)
        self.t2.forward(10)
        self.feast()
    def move_down(self):
        self.t2.seth(270)
        self.t2.forward(10)
        self.feast()

x = Display()

