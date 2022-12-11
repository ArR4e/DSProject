with open('kinganumbrid.txt', 'r') as f:
    numbrid = f.readlines()

for number in numbrid:
    try:
            print(round(2 / 3 * (float(number) - 2)))
    except:
            print('Vigane sisend')
