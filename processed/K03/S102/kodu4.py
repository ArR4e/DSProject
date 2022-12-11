f=open("kinganumbrid.txt","r")
a="sone"
b=0
while a!="":
    a=f.readline()
    try:
        b=2/3*(float(a)-2)
        print(round(b))
    except:
        print('Vigane sisend')
f.close()