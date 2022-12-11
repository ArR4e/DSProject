inp = open("kinganumbrid.txt","r")
numbrid = inp.readlines()

for x in numbrid:
    try:
        num = float(x)
        print(round(2/3 * (float(x) - 2)))
    except ValueError:
        print ("Vigane sisend")
    