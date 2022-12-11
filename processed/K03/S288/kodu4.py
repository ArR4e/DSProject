f = open('kinganumbrid.txt')

for x in f:
    try:
        float(x)
        x = 2 / 3 * (float(x) - 2)
        print(round(x))
    except ValueError:
        print('Vigane sisend')

f.close()