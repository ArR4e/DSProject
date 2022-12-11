from math import ceil
liin = int(input("Sisesta liinipikkus (täisarvuna meetrites): "))
kaug = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
post= (ceil(liin/kaug))+1
print("Liini ehitamiseks on minimaalselt vaja "+str(post)+" posti.")

