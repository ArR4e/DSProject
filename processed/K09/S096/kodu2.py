# minu_shuffle

import random

def minu_shuffle(jrj):
    jrj2 = jrj[:] #Teen uue järjendi, et olla kindel et kõik elemendid saaks muudetud
    
    # Käib läbi sisestatud järjendi element haaval ja muudab vastavad elemendid kasutades uut järjendit
    for i in range(len(jrj)):
        x = random.choice(jrj2)
        jrj[i] = x
        jrj2.remove(x)  #Eemaldab kasutatud elemendi järjendist

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(a)
minu_shuffle(a)
print(a)