kinganumbrid= open("kinganumbrid.txt", "r")
numbrid= (kinganumbrid.read().splitlines())

for line in numbrid:
    
    try:
        a= (2/3)*(float(line) - 2)
        print((round(a)))                 
    except:
        print("Vigane sisend")