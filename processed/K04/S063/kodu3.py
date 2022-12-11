import turtle
import random

turtle.pensize(3)
turtle.screensize(2000, 1500)

def korraparane_hulknurk(kylgede_arv, kyljepikkus):
    poore = 180*(kylgede_arv - 2)/kylgede_arv
    color = random.choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 'purple',
                    'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime', '#f55c4b'])
    turtle.color("black", color)
    turtle.begin_fill()
    for i in range(kylgede_arv):
        turtle.forward(kyljepikkus)
        turtle.right(180 - poore) # päripäeva
    turtle.end_fill()

def suvaline_koht():
    turtle.up()
    turtle.left(90)
    turtle.forward(random.randint(50, 300))
    turtle.down()

for i in range(30):
    korraparane_hulknurk(random.randint(3, 9), random.randint(20, 100))
    suvaline_koht()
    i += 1


turtle.exitonclick()
