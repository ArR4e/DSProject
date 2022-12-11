with open('kinganumbrid.txt', 'r') as ava_fail:
    for rida in ava_fail:
        try:
            print((round(2 / 3 * (float(rida) - 2))))
        except:
            print('Vigane sisend')