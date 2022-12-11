vanafail = open(input("Sisesta failinimi, mida on vaja tõlkida: "), "r")
uusfail = open(input("Sisesta failinimi, kuhu ilmub tõlgitud tekst: "), "w")
tekst = list(vanafail.readlines())
asendused = 0
for x in tekst:
    asendused += int(x.count("Hello"))
    uusfail.write(x.replace("Hello", "Tere"))
uusfail.close()
print("Tehti " + str(asendused) + " asendamist.")