pikkus = int(input("Sisesta elektriliini pikkus meetrites: "))
postide_vahe = int(input("Sisesta maksimaalne kõrvuti olevate postide kaugus meetrites: "))
postide_arv = pikkus // postide_vahe + 1
print("Elektriliini pikkus on", pikkus, "m")
print("Kõrvuti asetsevate postide maksimaalne vahemaa on", postide_vahe, "m")
print("Elektriliini ehitamiseks läheb vaja", postide_arv, "posti")