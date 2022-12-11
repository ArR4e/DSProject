f = open('taksohinnad.txt')
rida = ''
odavaim = ''
tee_pikkus = float(input('Sisestage tee pikkus kilomeetrites: '))

def tasu(istumis_hind, km_hind) :
    return istumis_hind + (tee_pikkus * km_hind)

for i in f :
    rida = i.strip().split(',')
    if odavaim == '' :
        odavaim = rida
        continue
    if tasu(float(rida[1]), float(rida[2])) < tasu(float(odavaim[1]), float(odavaim[2])) :
        odavaim = rida

print(f'Kõige odavam on {odavaim[0]}.')
    

f.close