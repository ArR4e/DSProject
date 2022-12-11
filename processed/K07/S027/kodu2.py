f = open('taksohinnad.txt')
tee = float(input('Sisesta teepikkus kilomeetrites: '))
hind_odav = 9999999999
firma_odav = ''

for rida in f:
    rida = rida.split(',')
    firma = str(rida[0])
    hind = tee * float(rida[2]) + float(rida[1])
    if hind < hind_odav:
        hind_odav = hind
        firma_odav = firma
print('kõige odavam on ' + firma_odav)