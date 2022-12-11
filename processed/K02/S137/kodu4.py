vana = input("Sisesta failinimi: ")
uus = input("Sisesta uue failinimi: ")
vana = open(vana)
vanatekst = vana.read()
y = vanatekst.count("Hello")
print("Tehti",y,"asendamist.")
#print(vanatekst)
vana.close()

uus = open(uus, "w")
uustekst = vanatekst.replace("Hello", "Tere")

uus.write(uustekst)
#print(uustekst)
uus.close()

