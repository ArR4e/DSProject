f = open("kinganumbrid.txt")
for i in f:
    n = f.readline()
    if type(n) == int or type(n) == float:
        print(round(2/3*(n-2)))
    else:
        print("Vigane sisend")