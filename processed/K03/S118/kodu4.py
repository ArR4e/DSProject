kinganumbrid = open("kinganumbrid.txt", "r")

for rida in kinganumbrid.readlines():
    try:
        kinga_number = float(rida)
        print(round(2/3*(kinga_number-2)))
    except:
        print("Vigane sisend")
        
kinganumbrid.close()