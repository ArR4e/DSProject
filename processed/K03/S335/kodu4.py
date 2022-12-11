f = open("kinganumbrid.txt")
while True:
    try:
        kinganumber = f.readline()
        if float(kinganumber) > 0:
            pikkus = kinganumber.replace(kinganumber, str(2 / 3 * (float(kinganumber) - 2)))
            print(round(float(pikkus)))
    except:
        print("Vigane sisend.")
        if kinganumber == "":
            break