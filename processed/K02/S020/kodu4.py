lahtefail = input("Lähtefaili nimi:")
sihtfail = input ("Sihtfaili nimi:")

fail = open(lahtefail)
lahtefaili_sisu = fail.read()
print(lahtefaili_sisu.count("Hello"))
sihtfaili_sisu = lahtefaili_sisu.replace("Hello", "Tere")
sihtfail = open(sihtfail, "+w")
sihtfail.write(sihtfaili_sisu)

fail.close()
sihtfail.close()