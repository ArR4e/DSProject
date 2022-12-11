fail = open('kinganumbrid.txt', encoding='UTF-8')

jalg = []

for rida in fail:
    nr = rida.strip('\n')
    jalg.append(nr)

fail.close()

for a in jalg:
    try:
        pikkus = 2/3 * (float(a)-2)
        print(round(pikkus))
    except:
        print('Vigane sisend')
        