# 2. minu_shuffle
#Pythoni moodulis random on funktsioon shuffle, mis ajab argumendiks antud järjendis elementide järjekorra
# juhuslikult segamini:
 
# >>> from random import shuffle
# >>> a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
# >>> shuffle(a)
# >>> a
# [5, 3, 6, 5, 5, 3, 4, 1, 6]
# Kirjuta ise analoogne funktsioon minu_shuffle, seejuures pole lubatud kasutada olemasolevat shuffle-funktsiooni.

# Automaatkontroll. Tuleks jälgida, et funktsioon tõstaks elemendid ümber talle etteantud listis,
# mitte ei tagastaks uut listi.

from random import randint

def minu_shuffle(a):
    indeksid = []
    for i in range(len(a)):
        indeksid.append(i)

    uus_indeks = []
    while len(uus_indeks) < len(indeksid):
        idx = randint(0, len(a)-1)
        if idx not in uus_indeks:
            uus_indeks.append(idx)
            continue
        else:
            continue
    
    # Järgneva koodirea kirjutamiseks pidin otsima abi Internetist (olles küll eelnevalt kasutanud murelahendajat, mis ei aidanud).
    # Viidatava allika näites lahendatakse sarnast probleemi. Kirjutasin allikas toodud näite ümber, ja sain aru, mida seal tehti.
    # Allika link: https://stackoverflow.com/questions/2177590/how-can-i-reorder-a-list
    a[:] = [a[i] for i in uus_indeks]
    print(a)