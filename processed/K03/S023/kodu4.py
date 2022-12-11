fail = open("kinganumbrid.txt")
for i in fail:
    i = i.strip()
    try:
        i  = float(i)
        print(round(2/3*(i-2)))
    except:
        print("Vigane sisend")