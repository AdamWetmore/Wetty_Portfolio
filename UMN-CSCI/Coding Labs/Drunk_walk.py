import turtle
import random

#===============================================================#
#                                                               #
#   The purpose of this lab was to write a code that simulated  #
#   a college student walking home from a bar after a night     #
#   of "not drinking". The goal was to see how long it would    #
#   take them to get out of the downtown area they were in.     #
#                                                               #
#===============================================================#

def Drunk_walk():
    counter = 0
    turtle.speed(0)
    while (turtle.xcor() > -300 and turtle.xcor() < 300 and turtle.ycor() > -300 and turtle.ycor() < 300): 
        direction = random.randint(1,4)
        turtle.lt((direction * 90) - 90)
        turtle.fd(30)
        counter += 1
    turtle.penup()
    turtle.home()
    turtle.write(counter)

Drunk_walk()
