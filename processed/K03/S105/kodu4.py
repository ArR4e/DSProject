f=open("kinganumbrid.txt")

while True:
    
    fail=f.readline()
    
    if fail=="":
        break

    try:
        x=(2/3 * (float(fail) - 2))
        print(str(round(x)))
    
    except:
        print("Vigane sisend")