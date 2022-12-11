f=open("kinganumbrid.txt","r")
sisu=f.readlines()
f.close()
vastus=[]
for a in sisu:
    try:
        vastus.append(round(2/3*(float(a)-2)))
    except:
        vastus.append("Vigane sisend")
        continue
for a in vastus:
    print(a)