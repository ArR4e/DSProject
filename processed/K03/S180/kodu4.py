f = open('kinganumbrid.txt', 'r')

for line in f:
    try:
        kinganr = float(line.strip())
        pikkus = 2 / 3 * (kinganr - 2)
        pikkus = round(pikkus)
        print(pikkus)
    except:
        print("Vigane sisend")