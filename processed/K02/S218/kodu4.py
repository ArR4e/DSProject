lähtefail = input("Mis on esimese faili nimi? ")
sihtfail = input("Mis on teise faili nimi? ")

f_esimene = open(lähtefail)
sisu = f_esimene.read()
f_esimene.close()

asendus = sisu.count("Hello")
sisu_uus = sisu.replace("Hello", "Tere")


f_teine = open(sihtfail, "w")
f_teine.write(sisu_uus)
f_teine.close()

print("Tehti " + str(asendus) + " " + "asendamist.")
