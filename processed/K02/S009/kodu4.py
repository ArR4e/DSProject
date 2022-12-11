esialgne_fail = input("Palun sisesta olemasoleva tektifaili nimi: ")
uus_fail = input("Palun sisesta uue tekstifaili nimi: ")

f = open(esialgne_fail)

faili_sisu= f.read()
print(faili_sisu + "\n")

f.close()

lähtefail = esialgne_fail
sihtfail = uus_fail
sihtfail_sisu = faili_sisu.replace('Hello','Tere')
print(sihtfail_sisu + "\n")

f = open(uus_fail,"w")
f.write(sihtfail_sisu)
f.close()

asendus = str(faili_sisu.count('Hello'))

print("Lähtefaili nimi: " + lähtefail)
print("Sihtfaili nimi: " + sihtfail)
print("Tehti " + asendus + " asendamist.")