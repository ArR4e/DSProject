#alustasin 20.09.2021 (17:09)
from turtle import *

def hulk_nurk(arv, pikkus):
    for i in range(arv): #kasutasin for tsükkli, sest teadsin juba enne kursust kuidas seda Pythonis kasutada
        forward(pikkus)
        right(360 / arv)
arv = int(input('Sisestage küldege arv: '))
pikkus = int(input('Sisestage külje pikkus: '))

hulk_nurk(arv, pikkus)

exitonclick()