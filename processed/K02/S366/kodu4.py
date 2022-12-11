lahtefail = input("Sisestage tekstifaili nimi: ")
sihtfail = input("Sisestage failinimi: ")

f = open(lahtefail)
faili_sisu = f.read().replace("Hello", "Tere")


f2 = open(sihtfail, "w")
f2.write(faili_sisu)
arv = faili_sisu.count("Tere")
print(arv)

f.close()
f2.close()

