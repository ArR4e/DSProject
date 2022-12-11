f=open("kinganumbrid.txt")
while True:
    numbrid=f.readline()
    if numbrid=="":
        break
    else:
        try:
            numbrid = float(numbrid)
            print(round((2/3)*(numbrid-2)))
        except:
               print("vigane sisend")
f.close()