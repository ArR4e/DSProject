from turtle import *
def fraktal(n, pikkus):
    if n <= 0:
        return True
    elif n == 1:
        for i in range(4):
            forward(pikkus)
            left(90)
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            left(180)
            if i < 3:
                fraktal(n-1, pikkus/2)
            left(180)
fraktal(1,100)                
  