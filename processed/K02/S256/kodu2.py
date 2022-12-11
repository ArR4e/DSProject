maks = float(input("sisesta liinipikkus: "))
vahe = float(input("sisesta max kaugus kahe posti vahel: "))

if maks > vahe and maks % vahe == 0:
    print("min kogus poste: ", round(maks // vahe +1))
elif maks > vahe and maks % vahe > 0:
    print(" postide arv: ", round(maks // vahe +2))
elif maks == vahe:
    print ("postide arv: ", 2)
elif maks < vahe:  
    print("Min kogus poste on:" , 2)

