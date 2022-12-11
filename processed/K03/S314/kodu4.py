f = open("kinganumbrid.txt")

while True:
    kinganumber = f.readline()
    if kinganumber == "":
        break
    try:
        print(round(2/3 * (float(kinganumber) - 2)))
    except:
        print("Vigane sisend")
    