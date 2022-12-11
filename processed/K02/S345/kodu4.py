failinimi = input("Sisestage lähtefaili nimi: ")
uusfailinimi = input("Sisestage sihtfaili nimi: ")

fail = open(failinimi)
uusfail = open(uusfailinimi, "w")

sisu = fail.read()
tolge = sisu.replace("Hello", "Tere")
uusfail.write(tolge)
print(tolge)
asendused = int(sisu.count("Hello"))
print("Tehti " + str(asendused) + " asendamist.")

fail.close()
uusfail.close()