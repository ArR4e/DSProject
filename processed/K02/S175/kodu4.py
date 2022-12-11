esialgne = input("Esialgne tekstifail: ")
uus = input("Uus tekstifail: ")

f = open(esialgne)

f.readline(1)
f.readline(2)
f.readline(3)
f.readline(4)
f.close()

tere = ("tere")
tere_Tere_Tere = ("Terebello")
tereTeretere = ("Tere! Tere! Tere!")
tere_seal = ("Tere seal")

f = open(uus, "w")

f.write(tere + "\n")
f.write(tere_Tere_Tere + "\n")
f.write(tereTeretere + "\n")
f.write(tere_seal + "\n")
f.close()

asendus = 'tere'.count('tere')
asendus2 = 'Terebello'.count('Tere')
asendus3 = 'Tere! Tere! Tere!'.count('Tere!')
asendus4 = 'Tere seal' .count('Tere')
                                     

print("Tehti ", int(asendus) + int(asendus2) + int(asendus3) + int(asendus4), "asendamist.")
