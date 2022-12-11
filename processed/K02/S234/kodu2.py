pikkus=int(input("maksimaalne pikkus"))
kaugus=int(input("maksimaalne kaugus"))
if kaugus>pikkus:
    print(2)
elif pikkus%kaugus==0:
    print(int(pikkus//kaugus)+1)
else:
    print(int(pikkus//kaugus)+2)