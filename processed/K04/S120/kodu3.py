from turtle import *
from random import randint

speed(0)

def draw_polygon(num_of_sides, side_length):
    angle = ((num_of_sides - 2) * 180) / num_of_sides
    
    for _ in range(num_of_sides):
        forward(side_length)
        left(180 - angle)

for _ in range(30):
    rand_x = randint(-400, 400)
    rand_y = randint(-300, 300)
    penup()
    goto(rand_x, rand_y)
    pendown()
    draw_polygon(randint(3,20), randint(30, 100))

exitonclick()