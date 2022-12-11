# parandatud hiljem

algfailinimi = input("Sisestage tõlgitava faili nimi: ")
uusfailinimi = input("Siestage uue faili nimi: ")

algfail = open(algfailinimi, "r", encoding="UTF-8")
uusfail = open(uusfailinimi, "w", encoding="UTF-8")

failisisu = algfail.read()
asendused = failisisu.count('Hello')
failisisu = failisisu.replace('Hello', 'Tere')
uusfail.write(failisisu)

algfail.close()
uusfail.close()

print("Tehti " + str(asendused) + " asendamist." )