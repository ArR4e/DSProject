pikkus1 = int(input("Sisesta liini pikkus meetrites: "))
pikkus2 = int(input("Sisesta postidevahline maksimaalne kaugus meetrites: "))
postide_arv = int(pikkus1 / pikkus2 + 1)
if postide_arv <= 1:
    print("Sellist elektriliini ei saa antud mõõtmetega ehitada.")
else:
    print("Minimaalne postide arv elektriliini ehitamiseks on: " + str(postide_arv))
