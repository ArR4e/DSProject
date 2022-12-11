from turtle import *
def f(sugavus, pikkus=100, suund=90):
    for i in range(3):
        forward(pikkus)
        if sugavus>1:
            f(sugavus-1,pikkus/2, -suund)
        rt(suund)
    fd(pikkus)
    rt(suund)

exitonclick()
        