sisu = open("kinganumbrid.txt", encoding="UTF-8")

while True:
    kinganumber = sisu.readline().strip()
    try:
        print(round((2/3)*(float(kinganumber) - 2)))
    except:
        if kinganumber == "":
            break
        else:
            print("Vigane sisend")
    