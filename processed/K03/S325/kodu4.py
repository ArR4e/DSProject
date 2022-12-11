fail = open("kinganumbrid.txt","r")
nr = fail.readlines()
i=0
imax = len(nr)
while i<imax:
    try:
        print(int(2/3*(float(nr[i].strip())-2)))
        i += 1
    except:
        print("Vigane sisend")
        i += 1