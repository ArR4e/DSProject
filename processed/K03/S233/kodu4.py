fail1 = open("kinganumbrid.txt")

for rida in fail1:
    try:
        print(round(2/3*(float(rida)-2)))
    except:
        print("Vigane sisend")