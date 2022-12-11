lähtefail = input("Sisesta lähtefaili nimi: ")
sihtfail = input("Sisesta sihtfaili nimi: ")

f = open(lähtefail)
g = open(sihtfail, "w")

lähtefaili_sisu = f.read()
g.write(lähtefaili_sisu.replace("Hello", "Tere"))
print("Tehti", lähtefaili_sisu.count("Hello"), "asendamist.")

f.close()
g.close()