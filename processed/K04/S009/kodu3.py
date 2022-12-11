from turtle import *
from random import randint

def hulknurk():
    joonistatud_kylgi = 0
    kylg_arv = randint(4,7)
    kylg_pikkus = randint(4, 150)
    
    while joonistatud_kylgi < kylg_arv:
        forward(kylg_pikkus)
        left(360/kylg_arv)
        joonistatud_kylgi += 1
    def liikumine():
        edasi = randint(5, 200)
        up()
        forward(edasi)
        left(edasi)
        forward(edasi)
        down()
    liikumine()

def korrad(x):
    while x > 0:
        hulknurk()
        x -= 1
        # vihje, kuidas seda osa teha nii, et ei peaks hulknurga funktsiooni 30 korda kordama sain siit: https://stackoverflow.com/questions/9047985/how-do-i-call-a-function-twice-or-more-times-consecutively 
        
korrad(30)

exitonclick()