import re

def kattuvus(esimene,teine):
    if esimene != teine:  #kattuvus
        print("Paroolid ei kattu!")
        return True
    
    elif len(esimene) < 8: #pikkus
        print("Parool on liiga lühike!")
        return True
    
    elif sisaldus(esimene) == True: # tähed/numbrid
        print("Parool peab sisaldama tähti ja numbreid!")
        return True
    else:
        return False # kõik korras

def sisaldus(sõna):
    #x = sõna.isalnum()
    #x = re.search('[a-zA-Z]',sõna)
    x = any(c.isalpha() for c in sõna)
    y = any(c.isdigit() for c in sõna)
    if x == True and y == True:
        return False
    else:
        return True

kasutajanimi = input("Kasutajanimi: ")

while True:
    parool1 = input("Parool: ")
    parool2 = input("Korda parooli: ")
    if kattuvus(parool1,parool2) == True:
        continue
    else:
        break

parool = parool1 [::-1]
fail = open("users.txt", "w")
fail.write(kasutajanimi + ':' + parool)
fail.close()