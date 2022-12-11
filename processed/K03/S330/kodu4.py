f = open("kinganumbrid.txt")
ridu = len(f.readlines())
loetud_ridu = 0
f.close()
f = open("kinganumbrid.txt")
while loetud_ridu < ridu:
    loetud_ridu += 1
    try:
        a = int(f.readline())
        print(round((2 / 3) * (a - 2)))
    except:
        print("Vigane sisend")