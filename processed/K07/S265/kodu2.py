try:
    f=open('taksohinnad.txt', 'r')
    x = f.read().replace('\n', ',').split(',')
    f.close()
    distance = float(input('Sisesta distants: '))
    cheapestprice = 0
    cheapestcab = ''

    for i in x:
        if x.index(i) % 3 == 0:
            if cheapestprice == 0:
                cheapestprice = float(x[x.index(i)+1])+distance*float(x[x.index(i)+2])
                cheapestcab = i
            else:
                if float(x[x.index(i)+1])+distance*float(x[x.index(i)+2]) < cheapestprice:
                    cheapestprice = float(x[x.index(i)+1])+distance*float(x[x.index(i)+2])
                    cheapestcab = i
    print('Kõige odavam on',cheapestcab+'.')
except:
    print('Mingi huinja')