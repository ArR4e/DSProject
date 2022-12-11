lähtefail = str(input("Lähtefaili nimi: "))
sihtfail = str(input("Sihtfaili nimi: "))

fail1 = open(lähtefail, "r")
tekst = fail1.read()
sõna = tekst.count("Hello")
tekst = tekst.replace("Hello", "Tere")
print("Tehti " + str(sõna) + " asendamist")
fail1.close()

fail2 = open(sihtfail, "w+")
fail2.write(tekst)
fail2.close()