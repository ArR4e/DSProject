fail1 = input("Sisesta siia esimese faili nimi: ")
fail2 = input("Sisesta siia teise faili nimi: ")

f1 = open(fail1)
f2 = open(fail2, "a")

fl1 = f1.read()

f2.write(fl1.replace("Hello", "Tere"))

f1.close()
f2.close()

print("Failis tehti", str(fl1.count("Hello")), "muudatust!")