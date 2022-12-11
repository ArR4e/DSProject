f=open("kinganumbrid.txt")

while True:
    try:
        kinganumber=f.readline()
        if kinganumber=="":
            break
        pikkus = round(2/3 * (float(kinganumber) - 2),0)
        if pikkus%1==0:
            print(int(pikkus))
        else:
            print(pikkus)
    except:
        print("Vigane sisend :(")
        
        
f.close()