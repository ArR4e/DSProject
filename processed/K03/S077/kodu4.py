f=open("kinganumbrid.txt")

for rida in f: #https://progtugi.cs.ut.ee/#/ts/6130aa4ce857bcd80b0014d0/6130adfce857bcd80b0014d9
    try:  
        print(round(2/3*(float(rida)-2)))
    except:
        print("Vigane sisend")
    
