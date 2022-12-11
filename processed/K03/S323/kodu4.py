f = open("kinganumbrid.txt")

while True:
    rida = f.readline()
    if rida == "":
        break
    try:
        vastus = round(2 / 3 * (float(rida) - 2))
        print(vastus)
    except:
        print("Vigane sisend")