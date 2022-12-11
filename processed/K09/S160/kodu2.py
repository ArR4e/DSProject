#Randint selle p2rast, et kasutada seda kui mul vaja random int arvu
### Kasutasin interneti abi selle ülesande lahendamisel, tegin endale ka koodid arusaadavaks!!!
from random import randint

def minu_shuffle(a):
    
    indeksid = len(a)
    
    for i in range(indeksid):
        # Siin võtan listist suvalised arvud
        rand = randint(i, indeksid - 1)
        # Vahetan elementide kohad 2ra
        a[i], a[rand] = a[rand], a[i]
    return a

# Küsin kasutajalt, millist listi ta soovib, enteriga lõpetab list küsimise ja liigub funktsiooni täitmise juurde
try :
    x = []
    
    while True:
        x.append(int(input()))

except :
    print(minu_shuffle(x))