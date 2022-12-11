lähtefail = str(input("Lähtefaili nimi:"))
sihtfail = str(input("Sihtfaili nimi:"))

f = open(lähtefail)
faili_sisu = f.read()

a = str(faili_sisu.count("Hello"))
print("Tehti " + a + " asendust.")

f = open(sihtfail, "w")
f.write(faili_sisu.replace("Hello","Tere"))

#print(faili_sisu)
#print(faili_sisu.replace("Hello","Tere"))

f.close()