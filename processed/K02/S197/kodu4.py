lahtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

f = open(lahtefail)
faili_sisu = f.read()
f.close()

asendus = faili_sisu.count("Hello")
faili_sisu = faili_sisu.replace("Hello", "Tere")

f = open(sihtfail, "w")
f.write(faili_sisu)
f.close()

print("Tehti", asendus, "asendamist.")