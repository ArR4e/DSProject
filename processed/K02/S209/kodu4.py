esimene = input("Lähtefaili nimi: ")
teine = input("Sihtfaili nimi: ")

g = open(teine, "w+")
f = open(esimene)

kokku = f.read().count("Hello")
f.close()

f = open(esimene)
for rida in f:
    g.write(rida.replace("Hello", "Tere"))
    
print("Tehti", kokku, "asendust.")    
g.close()
f.close()