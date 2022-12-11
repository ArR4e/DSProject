x = str(input("Lähtefaili nimi: "))
y = str(input("Sihtfaili nimi: "))
f = open(x)
g = open(y, "w")

algne_sisu = f.read().replace("Hello", "Tere")

f.close()

g.write(algne_sisu)

g.close()

print(algne_sisu.count("Tere"))