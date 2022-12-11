alg = input("Sisestage algse faili nimi: ")
uus = input("Sisestage uue faili nimi: ")
af = open (alg, encoding = "UTF-8")
uf = open (uus, "w", encoding = "UTF-8")
sisu = af.read()

asendus = int(sisu.count("Hello"))

sisu.replace("Hello", "Tere")


uf.write(sisu.replace("Hello", "Tere"))

af.close()
uf.close()

print ("Tehti", asendus, "asendust.")
