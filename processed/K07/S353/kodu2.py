from math import inf
fail=open('taksohinnad.txt', encoding='UTF-8')
pikkus=float(input('Palun sisestage kaugus kodust kilomeetrites: '))
hind=inf
odavaima_sõne=''
for rida in fail:
    järjend=rida.split(sep=',')
    if float(järjend[1])+pikkus*float(järjend[2])<hind:
        hind=float(järjend[1])+pikkus*float(järjend[2])
        odavaima_sõne= järjend[0]+', '
    elif float(järjend[1])+pikkus*float(järjend[2])==hind:
        hind=float(järjend[1])+pikkus*float(järjend[2])
        odavaima_sõne+= järjend[0]+', '
if hind!=inf:
    print('Kõige odavam on:', odavaima_sõne.strip(', '))
else:
    print('Faili lugemisel tekkis probleem')
    