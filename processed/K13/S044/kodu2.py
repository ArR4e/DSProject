import turtle

def ruut(x):
    t = turtle.Turtle()
    t.fd(100/x)
    t.ld(90)
    t.fd(100/x)
    t.ld(90)
    t.fd(100/x)
    t.ld(90)
    t.fd(100/x)
    t.ld(90)

def ruudud(kordus):
    forward = 100
    s = turtle.getscreen()
    t = turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.left(90)
        if kordus > 1:
            for i in range(4):
                t.forward(50)
                t.left(90)
                if kordus > 2:
                    for i in range(4):
                        t.forward(25)
                        t.left(90)
                        if kordus > 3:
                            for i in range(4):
                                t.forward(12)
                                t.left(90)
                        t.left(180)
                t.left(180)
        t.left(180)      
        
