import math
liini_pikkus=float(input("Sisesta liini pikkus meetrites (täisarvuna): "))
postide_maksimaalkaugus=float(input("Sisesta kõrvuti asuvate postide maksimaalkaugus meetrites (täisarvuna): "))
postide_arv=float(liini_pikkus/postide_maksimaalkaugus)
print("Liini ehitamiseks on vaja minimaalselt " + str(math.ceil(postide_arv)+1) + " posti.")
