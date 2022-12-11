fail1 = input("Inglise keelse faili nimi: ")

lähtefail = open(fail1)
lähtefaili_sisu = lähtefail.read()

sihtfaili_sisu = (((lähtefail.read()).replace("hello", "tere")).strip())
fail2 = input("Eesti keelse faili nimi: ")

sihtfail = open(fail2, "w")
sihtfail.write(str(sihtfaili_sisu))

print("Tehti", (lähtefaili_sisu.count("hello")), "muudatust")

lähtefail.close()
sihtfail.close()

