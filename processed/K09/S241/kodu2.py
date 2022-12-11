import random
a = [1, 2] # järjend, mida segi ajada, piiramata pikkusega, võib sisaldada elemente tüübist integer, float, list, string
def minu_shuffle(x):
    pikkus=len(x) # järjendi elementide arv
    uus_järjend = [] # uus tühi järjend
    juhuslik_jada = random.sample(range(0,pikkus),pikkus) #juhuslike arvude järjend, mis on sama pikk nagu esialgne järjend ja elementide väärtus on vahemikus nullist järjendi pikkus miinus üheni
    for i in range(0,pikkus): #esialgsest järjendist liikmete tõstmine uude järjendisse toimub järjendi liikmete arv korda
        vana_järjendi_el = a[juhuslik_jada[i]] #esialgsest järjendist võetakse üks element, juhuslikult kohalt
        uus_järjend.append(vana_järjendi_el) #see juhuslikult kohalt võetud element pannakse uude järjendisse
    return(uus_järjend) # funktsioon tagastab uue järjendi; ülesandes oli öeldud, et TULEKS JÄLGIDA, et funktsioon tagastab sama järjendi
print(minu_shuffle(a))