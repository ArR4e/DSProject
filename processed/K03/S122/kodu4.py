f = open('kinganumbrid.txt', "r")

sisu = f.readlines()
ridu = len(sisu)
i = 0

while ridu > i:
    rida = sisu[i]
    i = i + 1
    try:
        nr = float(rida.strip())
        pikkus = round ( 2 / 3 * (nr - 2))
        print(pikkus)
    except:
        print('Vigane sisend')
    
f.close()