f = open("kinganumbrid.txt", "r")
nimekiri = f.readlines()
for x in nimekiri:
    pikkus = 2/3 * (x - 2)
    print(round(pikkus))
    
#edasi ma ei oska :(