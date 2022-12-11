from turtle import *
import random

colors=["red", "yellow", "orange", "green"]

speed(100)
color(random.choice(colors))
while True:
    forward(200)
    left(179)
    if abs(pos()) < 1:
        break
penup()

#ei saa aru kuidas teha nii, et iga joon oleks teist värvi