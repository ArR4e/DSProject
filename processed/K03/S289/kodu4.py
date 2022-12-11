f = open('kinganumbrid.txt', encoding="UTF-8")

for kinganumber in f:
    try:
        print(round(2 / 3 * (float(kinganumber) - 2)))
    except:
        print("Vigane sisend")
        


    




    