

a = input("Sisestage teepikkus  kilomeetrites")

def takso(a):
    kogulist = []
    algus = []
    kilomeeter = []
    fail  = open("taksohinnad.txt", encoding = "utf8")
    for i in fail:
        i = i.strip().split(",")
        algus.append(i[1])
        kilomeeter.append(i[2])
        print(algus)
        print(kilomeeter)
    maksitaksi = float(float(algus[0]) + float(kilomeeter[0])* a)
    sõps = float(float(algus[1]) + float(kilomeeter[1])* a)
    waldo = float(float(algus[2]) + float(kilomeeter[2])* a)
    if maksitaksi < sõps and maksitaksi < waldo:
        return print("Kõige odavam on Maksitaksi")
    elif sõps < maksitaksi and sõps < waldo:
        return print("Kõige odavam on Sõps veab")
    elif waldo < sõps and waldo < maksitaksi:
        return print("Kõige odavam on Waldo takso")
    
takso(7)