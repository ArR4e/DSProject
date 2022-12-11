a = input("sisestage esimese tekstifaili nimi")
b = input("sisestage teise tekstifaili nimi")



fail1 = open(a)
sisu1 = fail1.read()
esialgne = sisu1.count("Tere")
sisu1 = sisu1.replace("Hello", "Tere")

fail2 = open(b, "w")
fail2.write(sisu1)
fail2.close()
asendamised = int(sisu1.count("Tere")) - int(esialgne)


print("Tehti", asendamised, "asendamist.")