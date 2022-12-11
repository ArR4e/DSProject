with open ("kinganumbrid.txt","r") as f:
    l=f.readlines()
for i in l:
    try:
        i=float(i)
        i=2/3*(i-2)
        i=round(i)
        i=str(i)
        print(i)
    except:
        print("Vigane sisend") 
#ry:
 #   print("l")