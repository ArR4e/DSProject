tekstifail = open("kinganumbrid.txt", 'r')

kinganumbrid = tekstifail.readlines()

for rida in kinganumbrid:
    try:
        print(int(round( 2/3 * (float(rida) - 2))))
        
    except:
        print("Vigane sisend")