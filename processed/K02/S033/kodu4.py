f1 = open(input("Millist faili soovid avada? "))
sisu = f1.read()
asendus = sisu.count("Hello")
sisu = sisu.replace("Hello", "Tere")

f2 = open(input("Millisesse faili soovid kirjutada? "), "w")
f2.write(sisu)

print("Tehti " + str(asendus) + " asendamist.")

f1.close()
f2.close()