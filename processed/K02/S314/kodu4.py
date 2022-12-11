lähtefail = input("Sisesta lähtefaili nimi: ")
sihtfail = input("Sisesta sihtfaili nimi: ")
print("lähtefaili nimi: " + str(lähtefail))
print("sihtfaili nimi: " + str(sihtfail))

f = open(lähtefail, "r")
faili_sisu = f.read()
uus_sisu = faili_sisu.replace("Hello","Tere")
print("Tehtud muudatusi: " + str(faili_sisu.count('Hello')))
f.close()

f = open(sihtfail, "x")
f.write(uus_sisu)
f.close()