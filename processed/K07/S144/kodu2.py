teepikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
hind = float('inf')

with open('taksohinnad.txt') as f:
    for i in f:
        i = i.strip()
        andmed = i.split(',')
        if float(andmed[1]) + float(andmed[2]) * teepikkus < hind:
            odavaim_takso = andmed[:]
            hind = float(odavaim_takso[1]) + float(odavaim_takso[2]) * teepikkus
print('Odavaim takso on ' + odavaim_takso[0])