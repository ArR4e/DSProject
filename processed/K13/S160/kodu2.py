#https://stackoverflow.com/questions/59009062/generating-square-fractals-with-python

from turtle import Screen, Turtle

def fractal(tase, turtle, pikkus, suund = 90):
    for i in range(3):
        turtle.forward(pikkus)
        
        if tase > 1:
            fractal(tase-1,turtle,pikkus/2,-suund)
            
        turtle.right(suund)
    
    turtle.forward(pikkus)
    turtle.right(suund)
    
screen = Screen()    
turtle = Turtle()
turtle.speed(100)

fractal(6,turtle,100)

turtle.hideturtle()
screen.exitonclick()