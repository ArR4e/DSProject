f = open("kinganumber.txt", "r")

for x in f:
    if x.isnumeric(): #viga peaks olema siin... ei oska midagi muud asemele panna. 
        print (round(2/3 * (int(x)-2)))
    else:
        print("Vigane sisend")