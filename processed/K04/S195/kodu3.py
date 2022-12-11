from turtle import *
from random import *
def hulknurk(kylgarv, kylgpikk):
    i = 0
    kraadid = 360/kylgarv
    while i < kylgarv:
        forward(kylgpikk)
        left(kraadid)
        i = i + 1

for x in range (30):
    kylgarv = randint(3, 50)
    kylgpikk = randint(5, 200)
    hulknurk(kylgarv,kylgpikk)
