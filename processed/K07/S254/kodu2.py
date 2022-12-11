
#taksode nimi, sisseistumise hind ja kilomeetri hind

km = float(input('Sisesta kodutee pikkus km: '))
#km = 10.00

fail = open('taksohinnad.txt', encoding='UTF-8')

hinnad = []
taksod = []

for rida in fail:
    takso = rida.split(',')
    hind = float(takso[1]) + float(takso[2])*km
    hinnad.append(hind)
    taksod.append(takso[0])

try:
    odavaim = min(hinnad)
    odavaim_takso = taksod[hinnad.index(odavaim)]
except:
    odavaim_takso = '"puudub"'

print('Kõige odavam on', str(odavaim_takso) + '.')








fail.close()