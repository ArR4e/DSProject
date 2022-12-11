import math
liini_pikkus=int(input("Sisestage liini pikkus meetrites: "))
postide_kaugus=int(input("Sisestage maksimaalne postide kaugus meetrites: "))
postide_kogus=liini_pikkus/postide_kaugus+1
print("Vajalik postide kogus on " + str(math.ceil(postide_kogus)))
