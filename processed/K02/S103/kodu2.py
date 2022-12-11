import math

Liini_pikkus = int(input("Sisestage elektriliini pikkus täisarvuna meetrites: "))
postide_maksimaalkaugus = int(input("Sisestage postide maksimaalkaugus: "))

print(int(math.ceil(Liini_pikkus/postide_maksimaalkaugus + 1)))
    