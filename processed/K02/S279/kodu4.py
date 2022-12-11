lähtefail = input("Sisesta lähtefaili nimi: ")
sihtfail = input("Sisesta sihtfaili nimi: ")

f1 = open(lähtefail)
f1_sisu = f1.read()
asendused = f1_sisu.count("Hello")
f1.close()

f2 = open(sihtfail, "w")
f2_sisu = f1_sisu.replace("Hello", "Tere")
f2.write(f2_sisu)
f2.close()

print("Tehti", asendused, "asendust.")