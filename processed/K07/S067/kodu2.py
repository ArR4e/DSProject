def maksumus(pikkus):
    f = open('taksohinnad.txt')
    hinnad = []
    
    try:
        nimed = []
        while True:
            takso = f.readline().strip('\n').split(',')
            if takso == ['']:
                break
            hinnad.append(float(takso[1]) + float(takso[2]) * float(pikkus))
            nimed.append(takso[0])
        print('Kõige odavam on', nimed[hinnad.index(min(hinnad))] + '.')
    except:
        return 0
pikkus = float(input('Sisesta tee pikkus:'))
maksumus(pikkus)
    