teekond=float(input('Sisesta tee pikkus kilomeetrites: '))

f=open('taksohinnad.txt')

read=f.readlines()

f.close()

hinnad=[]
taksod=[]

for rida in read:
    rida=rida.strip()
    info=rida.split(',')
    hind=float(info[1])+teekond*float(info[2])
    hinnad+=[hind]
    taksod+=[info[0]]

odav=min(hinnad)

indeks=hinnad.index(odav)

print('Kõige odavam on',taksod[indeks]+'.')