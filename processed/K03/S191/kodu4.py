f=open("kinganumbrid.txt")

m=1
while m==1:
    try:
        try:
            a=f.readline()
            if type(int(a))==int or type(float(a))==float:
                pikkus=int(round((2*(int(a)-2))/3,0))
                print(pikkus)
        except:
            if type(float(a))==float:
                pikkus=int(round((2*(float(a)-2))/3,0))
                print(pikkus)
    except:
        if a=="":
            m=0
        else:
            print("Vigane sisend")
f.close()