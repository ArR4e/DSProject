vana_f = input("Sisestage esimene fail ")
uus_f = input("Sisestage teine fail ")
f1 = open(vana_f)
f2= open(uus_f, "w")
tekst = f1.read()
f1.close()
uus = tekst.replace("Hello", "Tere")

f2.write(uus)
f2.close()

mitu = tekst.split("Hello")
arvutus = len(mitu) -1
print("Tehti ", arvutus, " asendamist.")

