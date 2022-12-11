liiniPikkus = int(input("Sisesta liini pikkus: "))
maxKaugus = int(input("Sisesta maksimaalne postidevaheline kaugus: "))

lisaPoste = 1 if liiniPikkus % maxKaugus == 0 else 2
posteVaja = liiniPikkus // maxKaugus + lisaPoste


print(posteVaja)