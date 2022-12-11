from math import ceil

liini_pikkus = int(input("Sisesta liini pikkus täisarvuna (meetrites): "))
postide_max_kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus täisarvuna (meetrites): "))
if liini_pikkus > postide_max_kaugus:
    postid = ceil(liini_pikkus / postide_max_kaugus) + 1
else:
    postid = 2
print("Elektriliini ehitamiseks kulub minimaalselt " + str(postid) + " posti")
