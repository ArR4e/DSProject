liini_pikkus = int(input("Palun sisesta elektriliini pikkus (meetrites): "))
postidevaheline_max_kaugus = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus (meetrites): "))

postide_arv = liini_pikkus // postidevaheline_max_kaugus

if liini_pikkus < postidevaheline_max_kaugus or liini_pikkus % postidevaheline_max_kaugus > 0:
    min_postide_arv = postide_arv + 2
elif liini_pikkus == postidevaheline_max_kaugus:
    min_postide_arv = postide_arv + 1
elif liini_pikkus > postidevaheline_max_kaugus and postidevaheline_max_kaugus != 1:
    min_postide_arv = postide_arv + 2
else:
    min_postide_arv = postide_arv + 1

print("Elektriliini ehitamiseks on minimaalselt vaja " + str(min_postide_arv) + " posti.")