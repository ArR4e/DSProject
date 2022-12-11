from turtle import *

def knruut(serv,süg):
    speed(10)
    if süg >= 1:
        forward(serv)
        left(90)
        knruut(serv*0.5,süg-1)
        right(180)
        forward(serv)
        left(90)
        knruut(serv*0.5,süg-1)
        right(180)
        forward(serv)
        left(90)
        knruut(serv*0.5,süg-1)
        right(180)
        forward(serv)
        right(90)
knruut(100,3)
