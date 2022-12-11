f=open("kinganumbrid.txt","r")
while True:
    try:
        nr=f.readline()
        if nr=="":
            break
        nr=float(nr)
        pikkus=2/3*(nr-2)
        print(round(pikkus))
    except:
        print("Vigane sisend")