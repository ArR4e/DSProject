from turtle import *
def fraktal(n,d):
    speed(0)
    tracer(0, 0)
    counter_2 = 0
    counter_3 = 0
    if n>=1:
        if n == 1:
            while counter_2 < 3:
                forward(d)
                right(90)
                counter_2 += 1
            forward(d)
            left(90)
        else:
            while counter_3 <3:
                    forward(d)
                    left(90)
                    fraktal(n-1,d*0.5)
                    counter_3 += 1
            forward(d)
            left(90)
    update()
        