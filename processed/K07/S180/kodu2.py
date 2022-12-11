s = float(input('Sisesta tee pikkus kilomeetrites: '))

f = open('taksohinnad.txt', encoding='UTF-8')

takso_hind = []
nimetus = []

for rida in f:
    if rida == '':
        break
    takso = list(rida.strip().split(','))
    hind1 = float(takso[1]) + float(takso[2]) * s
    takso_hind = takso_hind + [hind1]
    nimetus = nimetus + [takso[0]]
    
if takso_hind == []:
    print('')
else:
    print('Kõige odavam on ', nimetus[takso_hind.index(min(takso_hind))])