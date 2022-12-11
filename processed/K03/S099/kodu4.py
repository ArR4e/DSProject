f = open("kinganumbrid.txt")

while True:
    i = f.readline().strip()
    if i != "":
        try:
            print(round(2 / 3 * (float(i) - 2)))
        except:
            print("Vigane sisend")
    else:
        break
        
    