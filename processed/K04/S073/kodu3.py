import turtle as trt
import random as rdm

def draw(t, edges, length):
    t.penup()
    t.setposition(rdm.randint(-300,300), rdm.randint(-300,300))
    t.pendown()
    for i in range(edges):
        t.forward(length)
        t.left(360/edges)


for _ in range(30):
    ed = rdm.randint(3,25)
    le = rdm.randint(20,50)
    draw(trt.Turtle(), ed, le)

trt.Screen().exitonclick()