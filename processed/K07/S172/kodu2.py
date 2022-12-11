def loe_andmed(fail):
    nimed = []
    alg_hinnad = []
    kilo_hinnad = []
    
    f = open(fail)
    for rida in f:
        andmed = rida.split(',')
        nimi = andmed[0]
        alg_hind = andmed[1]
        kilo_hind = andmed[2]
        nimed = nimed + [nimi]
        alg_hinnad = alg_hinnad + [float(alg_hind)]
        kilo_hinnad = kilo_hinnad + [float(kilo_hind)]
        
    f.close()
    
    return (nimed, alg_hinnad, kilo_hinnad)

(nimed, alg_hinnad, kilo_hinnad) = loe_andmed('taksohinnad.txt')

kokku_hinnad = []

tee = float(input('Sisesta tee pikkus kilomeetrites: '))
i = 0
while i < len(nimed):
    hind = alg_hinnad[i] + tee*kilo_hinnad[i]
    kokku_hinnad = kokku_hinnad + [hind]
    i += 1
    
vahim_hind = min(kokku_hinnad)
index = kokku_hinnad.index(vahim_hind)
nimi = nimed[index]

print('Kõige odavam on', nimi)