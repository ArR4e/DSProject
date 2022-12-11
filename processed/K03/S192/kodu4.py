kinganr = open('kinganumbrid.txt')
while True:
    sisu = kinganr.readline()
    if sisu == '': # Kontrollimaks faili lõppu
        break
    else:
        try: # Niikaua kui tegemist on arvuga, siis toimub tegevus try all
            sisu = float(sisu)
            print(round(2/3 * (sisu-2)))
        except: # Vastasel korral annab selle vaste, nt str korral.
            print('Vigane sisend')
kinganr.close()