import turtle as t
import random

def joonista(k, p):
    c = 360 / int(k)
    a = 0
    while a < k:
        t.left(c)
        t.forward(p)
        a += 1    


aa = 0
bb = 30

while aa < bb:
    t.pendown()
    x = round(random.uniform(00.00, 400.00),2)
    y = round(random.uniform(00.00, 400.00),2)
    kk = random.randint(3, 8)
    pp = random.randint(30, 100)
    joonista(kk, pp)
    t.penup()
    t.setposition(x, y)
    aa += 1
    