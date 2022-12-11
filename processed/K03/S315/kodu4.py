f = open("kinganumbrid.txt")

for rida in f:
    a = 0
    try:         
        kinganr = float(rida.strip())
        a += 2/3 * (kinganr-2)
        print(round(a))
        
    except:
        print("Vigane sisend")
    
    