fail = open("kinganumbrid.txt")
rida = fail.readline()
while rida:
    try:
        if float(rida) >=0:
            print(round((2/3*(float(rida)-2))))
    except:
        print("Vigane sisend")
    rida = fail.readline()
    

