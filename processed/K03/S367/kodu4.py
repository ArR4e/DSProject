f = open('kinganumbrid.txt')

for rida in f:
    
kinganumber = float(rida.strip())
try:
    pikkus = round(2/3*( kinganumber - 2))
    print( pikkus)
except:
    print("Vigane sisend")
f.close()