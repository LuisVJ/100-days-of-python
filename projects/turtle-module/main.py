#####Turtle Intro######

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)


######## Challenge 1 - Draw a Square ############

def draw_square(size):
    for i in range(4):
        tim.forward(size)
        tim.left(90)

# draw_square(100)

######## Challenge 2 Draw a Dashed Line ############

def draw_dashed_line(width, length):
    for i in range(round(length/width)):
        tim.forward(width)
        tim.up()
        tim.forward(width)
        tim.down()

#draw_dashed_line(10, 200)

######## Challenge 3 Draw poligons ############

def draw_poligon(sides):
    for i in range(sides):
        tim.forward(100)
        tim.right(360/sides)

def draw_poligons(max_sides):
    for i in range (3, max_sides):
        color = (random.random(),random.random(), random.random())
        tim.pencolor(color)
        draw_poligon(i)

#draw_poligons(10)

######## Challenge 4 random walk ############

def random_walk(steps):
    tim.pensize(10)
    tim.hideturtle()
    for i in range(steps):
        tim.pencolor((random.random(),random.random(), random.random()))
        tim.forward(25)
        tim.left(random.choice([0, 90, 180, 270]))

#random_walk(200)

######## Challenge 5 Draw a Spirograph ############

def draw_spirograph():
    tim.speed("fastest")
    for i in range(50):
        tim.pencolor((random.random(),random.random(), random.random()))
        tim.circle(100)
        tim.right(360/50)

draw_spirograph()



screen = t.Screen()
screen.exitonclick()