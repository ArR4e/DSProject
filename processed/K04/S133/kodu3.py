from turtle import *
a=0
def na(arv):
    if arv>2:
        hulknurk=180+180*(arv-3)
        nurk=int(180-hulknurk/arv)
        a=int(arv)
        while a > 0 :
            a = a - 1
            forward(100)
            left(nurk)
na(int(input("Milline on nurkade arv?  ")))