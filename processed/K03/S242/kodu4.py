f = open('kinganumbrid.txt')
while True:
    try:
        kinganumber = f.readline()
        kinganumber = float(kinganumber.strip())
        pikkus = 2/3 * (kinganumber - 2)
        pikkus = round(pikkus)
        print(pikkus)

    except:
        if kinganumber == "":
            break
        print("Vigane sisend")
