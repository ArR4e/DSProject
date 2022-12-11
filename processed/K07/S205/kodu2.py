def soodsaim_sõit():
    s = float(input('Sisesta tee pikkus kilomeetrites: '))
    with open('taksohinnad.txt', 'r', encoding='utf-8') as f:
        odavaim = 0
        firma = ''
        for rida in f:
            takso = rida.strip('\n').split(',')
            hind = float(takso[1])+float(takso[2])*s
            if not odavaim:
                odavaim = hind
                firma = takso[0]
            elif hind < odavaim:
                odavaim = hind
                firma = takso[0]
                
        print('Kõige odavam on ' + firma+ '.')

soodsaim_sõit()