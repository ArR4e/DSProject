i = open(input("Esialgne tekstifail: "))
e = open(input("Uus tekstifail: "), "w")

sisu = i.read()
asend = sisu.count("Hello")
eesti = sisu.replace("Hello", "Tere")
i.close()

e.write(eesti)
print("Tehti", str(asend), "asendust.")
e.close()
