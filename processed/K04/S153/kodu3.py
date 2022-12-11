from turtle import*
import random

#hulknurkade arv
y = 30

def hulknurgad(n, l):
    if n < 3:
        print("ei teki hulknurk")
    elif n == 3:
        forward(l)
        left(120)
        forward(l)
        left(120)
        forward(l)
    elif n == 4:
        forward(l)
        left(90)
        forward(l)
        left(90)
        forward(l)
        left(90)
        forward(l)
    else:
        #hulknurga sisenurga suurus
        x = 180 - (((n-2)*180)/n)
        while n > 0:
            forward(l)
            left(x)
            n -= 1
            if n == 0:
                break
    return

while y > 0:
    n = random.randrange(1, 10)
    l = random.randrange(50, 200)
    hulknurgad(n, l)
    up()
    left(random.randrange(0, 360))
    forward(random.randrange(100, 300))
    down()
    y -= 1
    if y == 0:
        break

        
            

