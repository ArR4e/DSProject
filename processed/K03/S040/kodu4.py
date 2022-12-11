f = open('kinganumbrid.txt', "r")
while True:
    line = f.readline()
    try:
        a = float(line)
        p = round(2/3 * (a - 2))
        print(p)
    except:
        print("Vigane sisend")
        break
f.close()