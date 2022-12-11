liinipikkus = int(input("Sisestage liini pikkus: "))
postivahe = int(input("Sisestage postidevaheline maksimaalkaugus: "))
if liinipikkus % postivahe == 0:
    print(int(liinipikkus / postivahe) + 1)
elif liinipikkus < postivahe:
    print(int(2))
else:
    print(int(liinipikkus / postivahe) + 2)