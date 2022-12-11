algne_fail = input("Sisestage esialgse faili nimi: ")
uus_fail = input("Sisestage uue faili nimi: ")
f = open(algne_fail, "r")
g = open(uus_fail, "w")

asendused = 0
for rida in f.readlines():
    while "Hello" in rida:
        rida = rida.replace("Hello", "Tere", 1)
        asendused += 1
    g.write(rida)

print("Tehti", str(asendused), "asendust")

f.close()
g.close()