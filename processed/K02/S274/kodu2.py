liini_pikkus = int(input("Sisesta liini maksimumpikkus meetrites: "))
max_postivahe = int(input("Sisesta maksimaalne postidevaheline kaugus meetrites: "))
if liini_pikkus % max_postivahe > 0:
    postide_arv = int((liini_pikkus / max_postivahe) +2)    
else:
    postide_arv = int((liini_pikkus / max_postivahe) +1)
print("Elektriliini rajamiseks läheb vaja", postide_arv, "posti.")