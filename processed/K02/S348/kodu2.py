from math import*

liini_pikkus = int(input("Sisestage liini pikkus täisarvuna meetrites: "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))
postide_arv = ceil(liini_pikkus / maksimaalkaugus + 1)
print("Postide arv elektriliini ehitamiseks on",postide_arv,)











