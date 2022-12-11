## Koosta argumentideta funktsioon bingo, mis genereerib bingonumbreid. 
## Funktsioon peab järjendina tagastama 5 arvu, millest 3 on vahemikus 1 kuni 10 ning 
## ülejäänud 2 on vahemikus 11 kuni 20.
## Funktsioon ei tohi lubada sellist olukorda, kus järjendisse jääksid korraga 1, 2 ja 3. 
## Sellisel juhul tuleb genereerida uued arvud.

from random import sample

def bingo():
    # tagastatav tulemus
    tulemus = []
    # järjend [1, 2, 3] erinevates variantides
    c = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    # esimene juhuslik järjend vahemikus 1..10 - 3 elementi
    a = []
    while True:
        a = sample(range(1, 11), 3)
        if a not in c:
            tulemus = tulemus + a
            break
    # teine juhuslik järjend vahemikus 11..20 - 2 elementi
    b = sample(range(11, 21), 2)
    tulemus = tulemus + b
    
    return tulemus