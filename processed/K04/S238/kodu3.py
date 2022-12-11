import turtle
from random import *
def hulkn(arv, pikkus):
    nurk = 360 / arv
    külg = pikkus
    while arv > 0:
        t.forward(külg)
        t.left(nurk)
        arv -= 1
        
t = turtle.Turtle()

kordi = 30
while kordi > 0:
    nurki = randint(3,20)
    pikk = randint(5,150)
    
    kordi -= 1
    hulkn(nurki,pikk)
    t.penup()
    t.goto(randint(-300,0), randint(0,300))
    t.pendown()
        
   
        
exitonclick()
