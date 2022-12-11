import turtle

def move_turtle():
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(150)
        turtle.right(90)
    
def fun(sügavus):
    if sügavus == 0:
        return end_fill
    elif sügavus == 1:
        move_turtle()
    elif sügavus > 1:
        turtle.left(90)
        turtle.forward(150)
        move_turtle()
        return fun(sügavus-1)
        
fun(4)
turtle.exitonclick()