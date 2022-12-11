import math
pikkus=int(input("Liini pikkus: "))
kaugus=int(input("Kõrvutiasetsevate postide maksimaalkaugus: "))
postid=pikkus/kaugus+1

print("Minimaalselt on vaja liini ehitamiseks", math.ceil(postid), "posti.")