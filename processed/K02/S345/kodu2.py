liinipikkus = int(input("Sisestage liini pikkus täisarvuna meetrites: "))
postidekaugus = int(input("Sisestage postidevaheline maksimaalkaugus meetrites: "))

if liinipikkus == postidekaugus:
    print(2)
elif postidekaugus == 1:
    print((liinipikkus // postidekaugus) + 1)
else:
    print((liinipikkus // postidekaugus) + 2)