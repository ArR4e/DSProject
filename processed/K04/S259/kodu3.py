from turtle import*
from random import randint #f to generate random numbers is randint()

hulknurk = 0
def hulknurk(nurgad, külg):
    i = 0
    while i < nurgad:
        i += 1
        fd(külg) #fd (distance) Parameters. distance – a number (integer or float) Move the turtle forward by the specified distance, in the direction the turtle is headed.
        right(360/nurgad)
        
hulk = 0
while hulk < 30:  #kutsub 30 korda f hulknurk() välja
    hulk += 1
    penup()
    goto(randint(-300, 250), randint(-300, 250))
    pendown()
    hulknurg(randint(3, 20), randint(10,60))

