import colorgram
import turtle as t 
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


tom = t.Turtle()
tom.hideturtle()
tom.up()
tom.speed("fastest")
t.colormode(255)

def draw_painting(size, gap, dot_size):
    start_position = (-size*gap/2, -size*gap/2)
    tom.setpos(start_position)
    for i in range(size):
        for j in range(size):
            dot_color = random.choice(rgb_colors)
            tom.dot(dot_size, dot_color)
            tom.forward(gap)

        tom.setpos(start_position[0], start_position[1] + (i+1)*gap)


draw_painting(10, 50, 22)

screen = t.Screen()
screen.exitonclick()