def odavaim(km, iste, nimed, vahemaa):
    hinnad = []
    for nimi in nimed:
        kmhind = km[nimi]
        istehind = iste[nimi]
        hinnad.append(iste[nimi]+km[nimi]*vahemaa)
    odavaim = nimed[hinnad.index(min(hinnad))]
    print('Kõige odavam on', odavaim)
    
teepikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
if teepikkus == 0:
    print('te ei vaja takso teenust')
else:    
    f = open('taksohinnad.txt', 'r', encoding='UTF-8')
    kmhind = {}
    istumisehind = {}
    nimed = []

    for line in f:
        jarjend = line.replace('\n', '').split(',')
        kmhind[jarjend[0]] = float(jarjend[2])
        istumisehind[jarjend[0]]= float(jarjend[1])
        nimed.append(jarjend[0])
    
    odavaim(kmhind, istumisehind, nimed, teepikkus)

    f.close()
        
            