from turtle import *
from math import *
import random

#sisenurga suuruse valem: a = ((n-2) * 180) / n

n = random.randint(3, 16)
pikkus = random.randint(0, 100)

def joonista(n, pikkus):
    if n <= 2:
        raise Exception('Nii ei saa rallit sõita!')
    joonistatud_külgi = 0
    while joonistatud_külgi < n:
        forward(pikkus)
        left(180 - ((n-2) * 180) / n)
        joonistatud_külgi += 1

def pane_hullu():
    joonistatud_hulknurki = 0
    while joonistatud_hulknurki < 30:
        joonista(n, pikkus)
        up()
        left(random.randint(0, 90))
        forward(random.randint(0, 200))
        down()
        joonistatud_hulknurki += 1
        
pane_hullu()