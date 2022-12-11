liini_pikkus = int(input("Liini pikkus: "))
postide_maksimaalkaugus = int(input("Kõrvuti asetsevate postide maksimaalkaugus: "))

postide_arv = liini_pikkus / postide_maksimaalkaugus
 
if 0 < postide_arv != 1 and postide_arv != 2:
    x = int(postide_arv) + 2

else:
    x = int(postide_arv) + 1

print("Liini ehitmiseks on minimaalselt vaja " + str(x) + " posti.")