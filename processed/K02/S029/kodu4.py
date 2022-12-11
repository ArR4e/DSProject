lahtefail = input("Sisestage inglise keelse teksti failinimi: ")
sihtfail = input("Sisestage eesti keelse teksti failinimi: ")

f = open(lahtefail)
faili_sisu = f.read().replace("Hello", "Tere")
print(faili_sisu)

f2 = open(sihtfail, "w")
f2.write(faili_sisu)
arv = faili_sisu.count("Tere")
print(arv)

f.close()
f2.close()