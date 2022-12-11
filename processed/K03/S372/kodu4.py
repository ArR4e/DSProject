fail = open("kinganumbrid.txt", encoding="UTF-8")
for rida in fail:
    try:
        kinganumber = float(rida)
        eu_number = round(2/3 * (kinganumber - 2))
        print(eu_number)
    except:
        print("Vigane sisend")