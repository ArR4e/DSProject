f = open("kinganumbrid.txt")

while True:
    kinganumber = f.readline()
    
    if kinganumber == "":
        break
    
    try:
        pikkus = 2/3 * (float(kinganumber.strip()) - 2)
        print(round(pikkus))
        
    except:
        print("Vigane sisend")
    
f.close()