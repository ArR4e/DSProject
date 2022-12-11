a = open("kinganumbrid.txt")


for line in a:
    try:
        b = float(line.strip())
        c = 2/3 * (b - 2)
        print(round(c))
    except:
        print("Vigane sisend")












    
    
a.close()