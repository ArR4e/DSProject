a = input("Lähtefaili nimi: ")
b = open(a)
faili_sisu = b.read()
c = input("Sihtfaili nimi: ")
d = open(c, "w") # "w" - uue faili loomine
e = faili_sisu.replace("Hello", "Tere")
d.write(e)
g = faili_sisu.count("Hello")
f = "Tehti "
i = " asendamist"
print(f + str(g) + i)
b.close()
d.close()
