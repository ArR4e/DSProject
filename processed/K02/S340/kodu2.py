liinipikkus = int(input("Sisesta liini pikkus täisarvuna meetrites: "))
maxvahe = int(input("Sisesta kõrvutiasetsevate postide minimaalkaugus täisarvuna meetrites: "))
if maxvahe < liinipikkus:
    print("Liini ehitamiseks on minimaalselt vaja" , round((liinipikkus / maxvahe) + 1) , "posti.")
elif maxvahe > liinipikkus:
    print("Liini ehitamiseks on minimaalselt vaja 2 posti.")