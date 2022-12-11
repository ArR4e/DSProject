#kodu4 - kinganumber
f = open("kinganumbrid.txt", "r")
for i in f:
    try:
        kinganumber = float(i.strip())
        print(str(round(2/3*(kinganumber-2))))
    except:
        print("Vigane sisend")
f.close()
