#Kusib kasutajalt millist faili soovitakse tolkida
Lahtefail = open(input("Sisestage lahtefaili nimi: "))
#Palub kasutajal sisestada uue tolgitud teksti faili nime
Sihtfail = str(input("Sisestage siia sihtfaili nimi: "))
#Loebb lahtefaili
Lahtefail = Lahtefail.read()
#Loeb kokku mitu asendust on vaja teha
Asendatud = Lahtefail.count("Hello")
#Tolgib teksti teise faili
Sihttekst = Lahtefail.replace("Hello", "Tere")
#Avab uue faili kuhu tolgitud tekst salvestada
Sihtfail = open(str(Sihtfail + ".txt"), "w")
#Kirjutab teksti uude faili
Sihtfail.write(Sihttekst)
#Paneb kinni tolgitud faili
Sihtfail.close()
#Kuvab tulemuse mitu asendust tehti
print("Tehti " + str(Asendatud) + " asendamist.")
