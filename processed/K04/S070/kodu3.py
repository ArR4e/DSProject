import turtle, random
def hulknurk(pikkus, tippu):
    nurkade_summa = (tippu - 2) * 180
    nurk = 180 - nurkade_summa / tippu
    for i in range (0, tippu):
        turtle.forward(pikkus)
        turtle.left(nurk)
    return
for j in range (0, 30):
    turtle.penup()
    turtle.goto(random.uniform(-600, 600), random.uniform(-600, 600))
    turtle.pendown()
    hulknurk(random.uniform(10, 50), random.randrange(3, 15))
turtle.exitonclick()
 