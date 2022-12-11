#Koosta argumentideta funktsioon bingo, mis genereerib bingonumbreid. Funktsioon peab järjendina tagastama 5 arvu,
#millest 3 on vahemikus 1 kuni 10 ning ülejäänud 2 on vahemikus 11 kuni 20.
#Funktsioon ei tohi lubada sellist olukorda, kus järjendisse jääksid korraga 1, 2 ja 3.
#Sellisel juhul tuleb genereerida uued arvud.
#Vihje. Kattumatute juhuslike arvude genereerimiseks saab kasutada funktsiooni sample teegist random
# (ettevaatust: funktsioonis range on vahemiku lõpp välja arvatud!):
# >>> from random import sample
# >>> sample(range(1, 5), 2)
# [4, 1]
# Näide funktsiooni tööst:
# >>> bingo()
# [8, 3, 5, 16, 11]
# Automaatkontroll. Funktsioon peab olema ilma parameetritega ning tagastama 5 täisarvust koosneva järjendi;
# täisarvude järjekord ei ole oluline.
# Kui oled juba hulk aega proovinud ülesannet iseseisvalt lahendada ja see ikka ei õnnestu,
# siis võib-olla saad abi murelahendajalt. Püütud on selgitada tüüpilisemaid probleemseid selgitada ja anda vihjeid.
from random import sample
def bingo():
    esimene_arv = sample(range(1,11), 3)
    if sum(esimene_arv) == 6:
        esimene_arv = sample(range(1,11), 3)
        return esimene_arv
    teine_arv = sample(range(11,21), 2)
    väljund = esimene_arv + teine_arv
    return väljund

    