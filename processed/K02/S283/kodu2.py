import math

liini_pikkus = int(input("Palun sisestage soovitud liini pikkus meetrites: "))
postide_kaugus = int(input("Palun sisestage postide omavaheline kaugus meetrites: "))
jagatis = math.floor(liini_pikkus/postide_kaugus)

if liini_pikkus <= postide_kaugus:
    print (2)
    
elif postide_kaugus == 1:
    postide_arv = int(jagatis + 1)
    print (postide_arv)
    
elif liini_pikkus > postide_kaugus:
    postide_arv = int(jagatis + 2)
    print (postide_arv)