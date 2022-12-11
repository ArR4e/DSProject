avatud = open("kinganumbrid.txt", "r")
rida = 0
for rida in avatud:
        try:
            sisu = float(rida)
            sisu += 1
            print(round(2/3 * sisu - 2))
        except:
            print("Vigane sisend")

avatud.close()