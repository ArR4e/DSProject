a = open("kinganumbrid.txt", "r")
for line in a:
    try:
        print(round(2/3 * (float(line)- 2)))
    except:
        print("Vigane sisend")
    
