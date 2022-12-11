pikkus = int(input("Sisestage elektriliini pikkus (m): "))
kaugus = int(input("Sisestage kõrvuti asetsevate elektripostide maksimaalkaugus (m): "))
postid = pikkus // kaugus
if kaugus == 1:
    print(postid + 1)
elif pikkus == kaugus:
    print(postid + 1)
else:
    print(postid + 2)