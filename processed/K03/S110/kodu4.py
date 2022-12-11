f = open('kinganumbrid.txt')

while True:
    try:
        rida = f.readline()
        if rida == '':
            break

        number = float(rida.strip())

        pikkus = 2/3 * (number - 2)
        ümar = round(pikkus)
        print(ümar)
        
    
    except:
        print('Vigane sisend')