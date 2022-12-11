lähtefail = input("Palun sisesta olemasoleva faili nimi: ")
sihtfail = input("Palun sisesta uue faili nimi: ")
print("Lähtefaili nimi: "+lähtefail)
print("Sihtfaili nimi: "+sihtfail)

f = open(lähtefail)
f_sisu = f.read()
hellod = "Hello"
tered = "Tere"
asendused = f_sisu.count(hellod)
f.close()

g = open(sihtfail, "w")
g.write(f_sisu.replace(hellod, tered))
g.close()

print("Tehti", asendused, "asendamist.")
