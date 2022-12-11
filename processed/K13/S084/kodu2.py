from turtle import *
suurus = 100
def fraktal(suurus, arv, pos):
    turtles = [Turtle(),Turtle(),Turtle()]
    turtles[0] = pos
    for t in turtles:
        t.seth(turtles[0].heading())
        t.ht()
        t.speed(0)
    turtles[1].up()
    turtles[2].up()
    turtles[0].down()
    turtles[0].right(90)
    turtles[0].fd(suurus)
    pos = turtles[0].pos()
    turtles[0].left(90)
    turtles[0].fd(suurus)
    turtles[1].goto(turtles[0].pos())
    turtles[0].left(90)
    turtles[0].fd(suurus)
    turtles[2].goto(turtles[0].pos())
    turtles[2].left(90)
    turtles[0].left(90)
    turtles[0].fd(suurus)
    turtles[0].right(270)
    turtles[0].goto(pos)
    if arv > 1:
        fraktal(suurus/2,arv-1, turtles[0])
        fraktal(suurus/2,arv-1, turtles[1])
        fraktal(suurus/2,arv-1, turtles[2])
fraktal(suurus, 4, getturtle())
done()