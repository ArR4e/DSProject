lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

f1 = open(lähtefail)
f2 = open(sihtfail, "w")

sisu = f1.readlines()

asendused = 0

for rida in sisu:
    asendused += rida.count("Hello")
    f2.write(rida.replace("Hello","Tere"))
    
print("Tehti " + str(asendused) + " asendamist.")

f1.close()
f2.close()
