#kodu4

file = open("kinganumbrid.txt", "r")

for row in file:
    try:
        print(round(2/3 * (float(row)-2)))
    except:
        print("Vigane sisend")