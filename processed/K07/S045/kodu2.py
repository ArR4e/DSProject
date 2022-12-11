def ava_fail(hinnakirja_fail):
    with open(hinnakirja_fail, 'r', encoding='UTF-8') as file:
        hinnakiri = file.readlines()
    korrastatud_hind = []
    for hind in hinnakiri:
        korrastatud_hind.append(hind.strip('\n').split(","))
    return korrastatud_hind

def leia_odavaim(tee_pikkus, hinnakiri):
    odavaim = 0
    odavaim_firma = ""
    for firma in hinnakiri:
        hind = float(firma[1]) + float(firma[2]) * tee_pikkus
        if odavaim == 0 or hind < odavaim:
            odavaim = hind
            odavaim_firma = firma[0]
    print(f'Kõige odavam on {odavaim_firma}.')
    
hinnakirja_fail = 'taksohinnad.txt'
hinnakiri = ava_fail(hinnakirja_fail)
tee_pikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
leia_odavaim(tee_pikkus, hinnakiri)