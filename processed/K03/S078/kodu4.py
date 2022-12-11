f = open("kinganumbrid.txt", encoding="UTF-8")
while True:
    try:
        kinganumber = f.readline()
        pikkus = round(2/3 * (float(kinganumber) - 2))
        print(pikkus)

    except:
        if kinganumber == "":
            break
        else:
            print("Vigane sisend")