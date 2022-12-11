pikkus = int(input("Sisesta liini pikkus täisarvuna: "))
vahe = int(input("Sisesta postide kaugus üksteisest täisarvuna: "))

if pikkus <= 0 or vahe <= 0:
    print("Sisestatud arvud ei sobi")
else:
    a = pikkus/vahe + 1

    if float(a) > int(a):
        a += 1

    print("Minimaalne postide arv on ", int(a))