from turtle import *


sisend=int(input("Sisesta täisarv: "))
def fraktaal(sügavus):
    global äär, pikkus

    for i in range(3):
        forward(pikkus)
        
        if sügavus > 1:
            pikkus=pikkus/2
            äär=-äär
            fraktaal(sügavus-1)
            äär=-äär
            pikkus=pikkus*2
        right(äär)
    forward(pikkus)
    right(äär)
    
äär=90
pikkus=90
print(fraktaal(sisend))