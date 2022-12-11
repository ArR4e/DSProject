import turtle
import random

def kujund(a, b):
    i = 0
    while i < a:
        turtle.forward(b)
        turtle.right(360/a)
        i += 1
j = 0
while j < 30:
    turtle.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    kylg_arv = random.randrange(3, 30)
    pikkus = random.randrange(15, 150)
    turtle.down()
    kujund(kylg_arv, pikkus)
    turtle.up()
    j += 1
    



    

    

