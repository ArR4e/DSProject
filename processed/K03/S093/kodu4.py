fail = open('kinganumbrid.txt')

suurused = fail.readlines()
fail.close()

for suurus in suurused:
    try:
        pikkus = round(2/3 * (float(suurus) - 2))
        print(pikkus)
    except ValueError:
        print("Vigane sisend")
        



