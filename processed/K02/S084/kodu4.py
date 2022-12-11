esimenef = input("Sisestage siseneva olemasoleva faili nimi: ")
teinef = input("Sisestage väljuva faili nimi: ")

#Avab faili ja loeb info
f = open(esimenef)
fsisu = f.read()
f.close()

#Vaatab palju asendusi vaja ja teeb asendused
asendusi = fsisu.count("Hello")
fsisu = fsisu.replace("Hello","Tere")

#Kirjutab sisu teise faili
f = open(teinef, "w")
f.write(fsisu)
f.close()

print(f"Teostati {asendusi} asendust")