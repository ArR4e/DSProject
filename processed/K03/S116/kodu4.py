fail = open("kinganumbrid.txt", "rt")

info = fail.readlines()

for line in info:
    try:
        print(int(round(2/3 * (float(line) -2))))
        
    except:
        print("Vigane sisend")
        
fail.close()
