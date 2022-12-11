import turtle, random 

def hulknurk():
    turtle.speed(5)
    turtle.penup()
    a = random.randint(-550, 550)
    b = random.randint(-300, 300)
    turtle.goto(a, b)
    turtle.pendown()
    külg = random.randint(3,10)
    pikkus1 = random.randint(20,80)
    pikkus = pikkus1
    külgi = külg
    nurgad = 360/külgi
    turtle.setpos(a, b)
    for i in range(külgi):
        turtle.forward(pikkus)
        turtle.left(nurgad)
    turtle.hideturtle()
i = 1
while i < 31:
    try:
        hulknurk()
        i += 1
    except:
        break