from math import ceil
fail = open("kinganumbrid.txt","r")

for rida in fail:
    rida = rida.strip()
    try:
        float(rida)
    except ValueError:
        print("Vigane sisend")
    else:
        print(ceil((2/3)*(int(ceil(float(rida))))-2))
        
fail.close()
        