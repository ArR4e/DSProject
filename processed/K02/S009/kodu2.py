liini_pikkus = int(input("Palun kirjuta siia liini pikkus (täisarvuna, meetrites) ja vajuta ENTER: "))
post_kaugus = int(input("Palun kirjuta siia kõrvuti asetsevate postide maksimaalkaugus (täisarvuna, meetrites) ja vajuta ENTER: "))

min_kogus= int(liini_pikkus / post_kaugus + 2)

if liini_pikkus < post_kaugus:
    print("Liini pikkus ei saa olla lühem, kui postide kaugus üksteisest.")
elif liini_pikkus == post_kaugus:
    print("Liini ehitamiseks on vaja minimaalselt 2 posti.")
else:
    print("Liini ehitamiseks on vaja minimaalselt " + str(min_kogus) + " posti")

