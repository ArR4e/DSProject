f = open('kinganumbrid.txt')
rida = f.readline().strip()

while rida:
    try:
        jalanr = float(rida)
        print(round(2/3*(jalanr - 2)))
        rida = f.readline().strip()
    except:
        print('Vigane sisend!')
        rida = f.readline().strip()
f.close()

