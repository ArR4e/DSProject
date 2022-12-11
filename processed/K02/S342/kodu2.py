from math import ceil, floor
pikkus = int(input("Sisestage liini soovitud pikkus: "))
kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
postid = ceil(pikkus / kaugus)
print(postid + 1)
#print("Elektriliini ehitamiseks kulub " + str(postid + 1) + " posti.")