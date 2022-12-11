import turtle as t
t.speed(0)
def fraktal(tase, pikkus):
    if tase == 1:
        for i in range(4):
            t.fd(pikkus)
            t.left(90)
            t.left(180)
    else:
        for i in range(4):
            t.fd(pikkus)
            t.left(90)
            if i <3:
                fraktal(tase-1,pikkus*0.5)
            t.left(180)
                

fraktal(4,100)
t.exitonclick()