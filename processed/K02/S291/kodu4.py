lahtefaili_nimi = input("Lähtefaili nimi: ")
sihtfaili_nimi = input("Sihtfaili nimi: ")

fail1 = open(lahtefaili_nimi)
faili_sisu = fail1.read()
asendamiste_arv = faili_sisu.count("Hello")

fail2 = open(sihtfaili_nimi, "w")
fail2.write(faili_sisu.replace("Hello", "Tere"))

print("Tehti " + str(asendamiste_arv) + " asendamist.")

fail1.close()
fail2.close()

