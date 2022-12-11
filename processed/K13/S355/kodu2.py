from turtle import Turtle, Screen

def fraktaal(level, t, pikkus, direction = 90):
    for elem in range(3):
        t.forward(pikkus)
        
        if level > 1:
            fraktaal(level-1, t, pikkus/2, -direction)
            
        t.right(direction)
        
    t.forward(pikkus)
    t.right(direction)

screen = Screen()
t = Turtle()
t.speed(10)

fraktaal(4,t, 100)

screen.exitonclick()

#Kasutasin ülesande lahendamisel StackOverflow artiklit:
#https://stackoverflow.com/questions/59009062/generating-square-fractals-with-python?fbclid=IwAR1hf1WkkNDMJXOtLXN5xA3iEu2c-zEyg4LG5L8K2iXw2rrcNj_MjooQB6Q