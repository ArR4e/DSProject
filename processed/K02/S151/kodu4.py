failinimi = input("Sisesta faili nimi, mida soovid tõlkida: ")
salvesta = input("Sisesta faili nimi, millena tõlge salvestatakse: ")

print()
f = open(failinimi+".txt")
faili_sisu = f.read()
print(faili_sisu)

t = open(salvesta+".txt", "w")
t.write(faili_sisu.replace("Hello", "Tere").replace("hello", "tere"))
t.close()

print()
k = open(salvesta+".txt")
tolge = k.read()
print(tolge)

print()
asendus1 = tolge.count("Tere")
asendus2 = tolge.count("tere")
print("Tehti ", asendus1+asendus2, " asendust.")

