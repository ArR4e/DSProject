#alustasin 23.11.2021 (20:36)
from turtle import *
def ruutude_fraktal(tase, pikkus):
    if tase >= 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                ruutude_fraktal(tase - 1, pikkus * 0.5)
            left(180)