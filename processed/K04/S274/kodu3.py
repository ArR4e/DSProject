from turtle import *
kylg = int(input("Sisesta hulknurga külgede arv: "))

def hulknurk():
    i = 0
    while i < kylg:
        forward(100)
        left(180 - (180*(kylg-2))/kylg)
        i+= 1

hulknurk()

up()
forward(100)
left(90)
forward(100)

hulknurk()

exitonclick()
