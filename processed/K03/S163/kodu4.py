file = open('kinganumbrid.txt', 'r')

for rida in file:
    try:
        kinganumber = float(rida)
        pikkus = 2/3 * (kinganumber - 2)
        print(round(pikkus))
    except:
        print('Vigane sisend')
        
file.close()
    
