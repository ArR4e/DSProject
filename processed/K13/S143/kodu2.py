from turtle import *

def fraktal(dep,l=100,a=0):
    if dep == 0:
        if a%2 == 1:
            right(90)
        else:
            left(90)
    else:
        #left(90)
        for i in range(3):
            forward(l)
            a+=1
            fraktal(dep-1,(l*0.5),a+1)
        forward(l)
fraktal(2)
