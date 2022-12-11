import turtle
from random import randint

def draw(amount, length):
    i = 1
    while i <= 30:
        turtle.penup()
        turtle.goto(randint(-400, 0), randint(0, 400))
        turtle.pendown()
        for _ in range(amount):
            turtle.forward(length)
            turtle.right(360 / amount)
        i+=1
        
            

draw(randint(0, 15), randint(0, 40))
    

    
    
    
    
    