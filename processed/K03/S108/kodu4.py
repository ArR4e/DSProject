fail=open("kinganumbrid.txt","r")
while True:
    try:
        kinganr=fail.readline()
        if kinganr=="":
            break
        kinganr=float(fail.readline())
        pikkus=round(2/3*(float(kinganr-2),0))
        print(pikkus)
    except:
        print("Vigane sisend")
            
        