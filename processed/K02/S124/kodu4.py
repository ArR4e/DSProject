a = input("Sisesta tõlgitava faili nimi: ")
c = input("Sisesta tõlgitud faili nimi: ")

print("\n")

print("Algne faili sisu: ")

f = open(a)
faili_sisu = f.read()
print(faili_sisu)
f.close()

print("\n")

print("Tehti " + (str(faili_sisu.count("Hello"))) + " asendust.")

tõlge = open(c, "w")
tõlge.write(str(faili_sisu).replace("Hello", "Tere"))
tõlge.close()

t = open(c)
tõlke_sisu = t.read()
print(tõlke_sisu)
t.close()




