lähtfail = str(input("Lähtefaili nimi: "))
sihtfail = str(input("Sihtfaili nimi: "))

f = open(lähtfail)
f_sisu = f.read()
f_arv = f_sisu.count("Hello")
f_asendus = f_sisu.replace("Hello", "Tere")
f.close()

g = open(sihtfail, "w")
g.write(f_asendus)
g.close()

print("Tehti " + str(f_arv) + " asendamist.")