algne = input("Lähtefaili nimi: ")
uus = input("Sihtfaili nimi: ")

inglise = open("inglise.txt", "r")
sisu = inglise.read()
inglise.close()
print("\nFaili inglise.txt sisu:\n" + str(sisu))

asendamiste_arv = sisu.count("Hello")
print("\nTehti " + str(asendamiste_arv) + " asendust.")
uus_sisu = sisu.replace("Hello", "Tere")


eesti = open("eesti.txt", "w")
eesti.write(uus_sisu)
eesti.close()

eesti = open("eesti.txt", "r")
print("\nFaili eesti.txt sisu:\n" + str(eesti.read()))
eesti.close()
