import math
a=open("kinganumbrid.txt")
for rida in a:
    try:
        if math.ceil(2/3*(float(rida.strip())-2))>=(2/3*((float(rida)-2))+0.5):
            print(round(2/3*(float(rida.strip())-2)))
        else:
            print(math.ceil(2/3*(float(rida.strip())-2)))
    except:
        print("vigane sisend")
    
