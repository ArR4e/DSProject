f = open("kinganumbrid.txt")
   
while True:
    try:
        while True:
            kinganumber = f.readline()
            a = kinganumber.strip()
            if kinganumber == "":
                break
            print(str(round(2/3 * float(a) - 2)))
    except:
        print("Vigane sisend")
        