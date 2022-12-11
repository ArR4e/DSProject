esimene = input ("Sisesta faili nimi: ")
teine = input ("Sisesta teine faili nimi: ")

fail = open(esimene)
fail2 =open (teine, "w")

sisu = fail.read()
helloarv = sisu.count("Hello")
uussisu= sisu.replace("Hello", "Tere")

print ("Tehti " + str( helloarv) + " asendamist.")

fail2.write(uussisu)

fail.close()
fail2.close()