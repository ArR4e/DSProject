fail = open('taksohinnad.txt', 'r')
 
km = float(input('Sisesta tee pikkus kilomeetrites: '))
odavam_hind = 1000
odavam_nimi = ''

for rida in fail:
    rida = rida.split(',')
    nimi = rida[0]
    stardi_hind = float(rida[1])
    km_hind = float(rida[2])
    
    hind = stardi_hind + km*km_hind
    if odavam_hind > hind:
        odavam_hind = hind
        odavam_nimi = nimi

print('Kõige odavam on ' + odavam_nimi + '.')

fail.close()