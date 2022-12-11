esimene = input("Sisesta esimene failinimi: ")
teine = input("Sisesta teine failinimi: ")


f = open(esimene)
g = open(teine, "w")
teisendusi = 0

for rida in f:
    teisendusi += rida.count("Hello")
    rida_e = rida.replace("Hello", "Tere")
    g.write(rida_e)
   

g.close()
f.close()

print(f"Tehti {teisendusi} teisendust")