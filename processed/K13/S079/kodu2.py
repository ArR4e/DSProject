# 2. Sarnaste ruutude fraktal
# Kirjuta rekursiivne funktsioon, mis joonistab kilpkonnaga fraktali ruudust,
# mille kolmes nurgas on sarnased ruudud ning nende kolmes nurgas on ka sarnased ruudud
# ja nii edasi vastavalt funktsioonile etteantud sügavusele.

# Joonisel on fraktalid, mis tekivad sügavuste 1, 2, 3 ja 4 puhul.

from turtle import *

def fraktal(sügavus, pikkus):
    speed(0)
    if sügavus == 0:
        return
    elif sügavus == 1:
        for i in range(4):
            forward(pikkus)
            right(90)
    else:
        for i in range(3):
            forward(pikkus)
            left(90)
            fraktal(sügavus-1, pikkus*0.5)
            left(180)
        forward(pikkus)
        right(90)
        
        
    