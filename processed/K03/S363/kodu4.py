f = open("kinganumbrid.txt", "r")

read = f.readlines()
pikkus = len(read)
n = 0

while n < pikkus:
    try:
        nr = float(read[n])
        jalg = 2/3 * (nr-2)
        suurus = round(jalg)
        print(int(suurus))
    
    except:
        print("Vigane sisend")
        
    n += 1
        