import turtle

def draw_triangle(t):
    for i in range(3):
        t.forward(50)
        t.left(120)

def draw_triangles(number,t):
    count = 0
    while number > count:
        draw_triangle(t)
        t.rt(360 / number)
        count += 1



