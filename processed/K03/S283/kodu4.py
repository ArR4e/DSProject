fail = open("kinganumbrid.txt")
while True:
    faili_sisu = (fail.readline().strip())
    if faili_sisu == "":
        break
    try:
        print(round(2/3 * (float(faili_sisu) - 2)))
    except:
        print("Vigane sisend")