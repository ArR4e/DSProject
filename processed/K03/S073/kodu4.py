file = open("kinganumbrid.txt", "r", encoding="UTF-8")


for line in file.readlines():
    try:
        print(str(round(2/3 * (float(line)-2))))

    except:
        print("Vigane sisend")
