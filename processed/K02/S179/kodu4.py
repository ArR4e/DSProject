lahtefail = open(str(input("Sisesta lähtefaili nimi: ")), "r")
tekst = lahtefail.read()
lahtefail.close()

tekst = tekst.replace("Hello", "Tere")
asendus = tekst.count("Tere")

sihtfail = open(str(input("Sisesta sisendfaili nimi: ")), "w")
sihtfail.writelines(tekst)
sihtfail.close()

print("Tehti",asendus,"asendust.")