tee_pikkus= float(input('Sisestage kodutee pikkus kilomeetites: '))

f= open('taksohinnad.txt', encoding='UTF=8')

taksode_hinnad=[]
nimed=[]
for rida in f:
    osad=rida.split(',')
    nimi=osad[0]
    sisseistumise_hind=float(osad[1])
    km_hind=float(osad[2])

    takso_hind= sisseistumise_hind+tee_pikkus*km_hind
    taksode_hinnad.append(takso_hind)
    nimed.append(nimi)
    väikseim= min(taksode_hinnad)
    indeks = taksode_hinnad.index(väikseim)
    
f.close()
    
print('Kõige odavam on', nimed[indeks])

