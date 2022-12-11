pikkus = int(input ("Sisesta liini pikkus: "))
kaugus = int(input ("Sisesta postide vaheline maksimaalne kaugus: "))
postid = int(pikkus/kaugus +2)
if pikkus == kaugus:
    print (2)
else:
    if pikkus / kaugus == 2:
        print (3)
    else:
        print (postid) 