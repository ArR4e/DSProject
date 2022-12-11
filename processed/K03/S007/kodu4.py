f=open("kinganumbrid.txt")

while True:
    kinganumbrid = f.readline().strip()
    
    if kinganumbrid =="":
        break
    try:
        kinganumbrid=float(kinganumbrid)
        x=(kinganumbrid-2)*2/3
        print(round(x))
    except:
        print("Vigane sisend")
f.close()
