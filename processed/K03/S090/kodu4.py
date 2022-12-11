f = open("kinganumbrid.txt", encoding="UTF-8")
for x in f:
    try:
        print(round(2/3*(float(x)-2)))
    except:
        print("Vigane sisend")
    