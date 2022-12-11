import math
liini_pikkus = int(input("Liini pikkus: "))
korvuti_kaugus = int(input("Kõrvutiasetsevate postide maksimaalkaugus: "))
umb_postid_maks_kaugusega = (math.ceil((liini_pikkus)/(korvuti_kaugus)))

umb_max_dist = (math.floor((liini_pikkus)/(umb_postid_maks_kaugusega)))
postid_kokku = math.ceil((liini_pikkus)/(umb_max_dist))

if liini_pikkus < korvuti_kaugus or liini_pikkus == korvuti_kaugus or (liini_pikkus - korvuti_kaugus) < 3 and (liini_pikkus - korvuti_kaugus) > 1:
    print("Liini ehitamiseks on minimaalselt vaja " + str(postid_kokku+1) + " posti.")
else:
    print("Liini ehitamiseks on minimaalselt vaja " + str(postid_kokku) + " posti.")