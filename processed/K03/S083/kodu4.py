fail = open('kinganumbrid.txt', 'r')
for rida in fail:
    try:
        kinganr = float(rida.strip())
        print(round(2/3*(kinganr-2)))
    except:
        print('Vigane sisend')
    