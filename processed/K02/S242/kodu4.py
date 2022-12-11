a = input("Sisesta olemasoleva faili nimi ")
b = input("Sisesta uue faili nimi ")
f = open(a, "r")
sisu = f.read()
print("Failis muudeti", sisu.count("Hello"), "sõna")
sisu = sisu.replace("Hello", "Tere")
f.close()
with open(b, "w") as t:
    t.write(sisu)