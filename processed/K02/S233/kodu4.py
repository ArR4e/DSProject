lahtefail = open(input("Lähtefaili nimi: "), "r")
sihtfail = open(input("Sihtfaili nimi: "), "w+")

asendused=0
for rida in lahtefail:
    asendused += rida.count("Hello")
    sihtfail.write(rida.replace("Hello", "Tere"))

print("Tehti " + str(asendused) + " asendust")

lahtefail.close()
sihtfail.close()
