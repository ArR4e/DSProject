from turtle import *
import random
screensize(500,500)
speed(-1)

def hulk(külgedearv, küljepikkus):
    if külgedearv > 2:
        for i in range(külgedearv):
            forward(küljepikkus)
            right(360/külgedearv)
    else:
        print("Sellist hulknurka ei ole olemas")

for i in range(30):
    up()
    goto(random.randint(-300,300),random.randint(-300,300))
    down()
    hulk(random.randint(3,15),random.randint(1,100))

exitonclick()