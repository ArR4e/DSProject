fail1 = input("sisestage faili nimi: ")
fail2 = input("sisestage teise faili nimi: ")

f = open(fail1)
failiSisu = f.read()
uusFailiSisu = failiSisu.replace("Hello", "Tere")
asendamiseArv = failiSisu.count("Hello")

f = open(fail2, "w")
f.write(uusFailiSisu)
print("Tehti", asendamiseArv, "asendamist")
f.close()