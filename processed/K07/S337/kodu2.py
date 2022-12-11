s = float(input('Sisesta tee pikkus kilomeetrites: '))
if s > 0:
    try:
        f = open('taksohinnad.txt')
        hinnad = []
        nimed = []
        for rida in f:
            nimi = rida.split(',')[0]
            sisse_hind = float(rida.split(',')[1])
            km_hind = float(rida.split(',')[2])
            hind = sisse_hind + km_hind*s
            hinnad.append(hind)
            nimed.append(nimi)
        f.close()
        index = hinnad.index(min(hinnad))
        print('Kõige odavam on', nimed[index]+'.')
    except:
        print('Sisendfail on vigase struktuuriga.')
else:
    print('Tee pikkus peab olema suurem kui 0 kilomeetrit.')
