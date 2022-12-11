liini_pikkus = int(input("liini pikkus: "))
posti_kaugus = int(input("postide kaugus: "))

vastus = int(liini_pikkus//posti_kaugus)

if liini_pikkus < posti_kaugus:
    print(vastus + 2)
elif liini_pikkus == posti_kaugus:
    print(vastus + 1)
else:
    if liini_pikkus > posti_kaugus and liini_pikkus % posti_kaugus == 0:
        print(vastus + 1)
    elif liini_pikkus > posti_kaugus:
        print(vastus + 2)
        