from math import ceil

liini_pikkus = int(input("Palun sisesta elektriliini pikkust (täisarvuna meetrites): "))
postide_maksimaalkaugus = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugust \
(täisarvuna meetrites): "))
postide_arv = 1 + (ceil(liini_pikkus / postide_maksimaalkaugus))
postid = str(postide_arv)

print("Liini ehitamiseks on vaja minimaalselt " + postid + " posti.")