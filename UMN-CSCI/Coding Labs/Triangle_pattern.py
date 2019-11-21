import turtle

def draw_triangles(number):
    count = 0
    while number > count:
        draw_triangle()
        turtle.rt(360 / number)
        count += 1
