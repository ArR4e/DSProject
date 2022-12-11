import math
liini_pikkus = int(input("Sisestage elektriliini pikkus: "))
max_kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))

min_postid = math.ceil((liini_pikkus/max_kaugus+1))

print(min_postid)