with open('kinganumbrid.txt', 'r') as f:
    for line in f:
        try:
            num = float(line.replace(',', '.'))
            print(round(2 / 3 * (num-2)))
        except:
            print('Vigane sisend')