fail1 = input ("Lähtefaili nimi: ")
fail2 = input ("Sihtfaili nimi: ")

esimeneFail = open(fail1)
sihtFail = open(fail2, "w")

sisu = esimeneFail.read()

helloCounter = sisu.count("Hello")
asendatudSisu = sisu.replace("Hello", "Tere")

print ("Tehti " + str (helloCounter) + " asendamist.")

sihtFail.write(asendatudSisu)

esimeneFail.close()
sihtFail.close()