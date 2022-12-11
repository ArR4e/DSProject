f=open('kinganumbrid.txt')
while True:
    try:
        kinganumber=f.readline()
        if kinganumber=="":
            break
        else:
            kinganumber1=float(kinganumber)
            pikkus=2/3*(kinganumber1-2)
            print(round(pikkus))
    except:
        print("Vigane sisend")
