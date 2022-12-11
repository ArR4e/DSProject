from turtle import *
import random
import math

speed(15)


kordade_arv = 0

def kolmnurk():
    külgi = 0
    while külgi < 3:
        forward(a)
        left(120)
        külgi += 1

def ruut():
    külgi = 0
    while külgi < 4:
        forward(a)
        left(90)
        külgi += 1

def viisnurk():
    külgi = 0
    while külgi < 5:
        forward(a)
        left(72)
        külgi += 1
        
def kuusnurk():
    külgi = 0
    while külgi < 6:
        forward(a)
        left(60)
        külgi += 1


        
while kordade_arv < 30:
    n = random.randint(3, 6)
    a = random.randint(10, 100)
    abtsiss = random.randint(-250, 250)
    ordinaat = random.randint(-250, 250)
    up()
    goto(abtsiss, ordinaat)
    down()
    if n==3:
        kolmnurk()
    elif n==4:
        ruut()
    elif n==5:
        viisnurk()
    elif n==6:
        kuusnurk()
    
    kordade_arv += 1
        