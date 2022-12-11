x = input("lähtefail: ")
y = input("sihtfail: ")
fail = open(x)
sisu = fail.read()
fail.close()
uus_sisu = sisu.replace("Hello", "Tere")

uusfail = open(y, "w")
uusfail.write(uus_sisu)
uusfail.close()

kogus = uus_sisu.count("Tere")
print("Tehti", kogus, "asendamist")
#Mul tuleb vastus 4 ja kõik toimib. Kontrollile miski ei meeldi ja ma ei mõista, mis see on.