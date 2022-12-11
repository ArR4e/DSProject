Fi = input("Sisesta ingliskeelse faili nimi: ") + ".txt"
Fe = input("Sisesta eestikeelse faili nimi: ")
esimene = open(Fi)
teine = open(Fe, "w")
a = 0
for hel in esimene:
    teine.write(hel.replace("hello", "Tere"))
    a += hel.count("hello")
print(a)
esimene.close()
teine.close()
