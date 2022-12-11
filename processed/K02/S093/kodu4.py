esimene = input("Sisestage 1.failinimi: ")
teine = input("Sisestage 2.failinimi: ")

file = open(esimene,"r")
text = file.read()
file.close()

changed = text.replace("Hello", "Tere")
file = open(teine, "w")
file.write(changed)
file.close()
