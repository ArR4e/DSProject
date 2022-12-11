f=open('taksohinnad.txt', encoding="UTF-8")
s=float(input('Sisestage teepikkus: '))
odavaim_hind=1000000
odavaim_firma=''
for takso in f:
    taksoS=takso.split(',')
    km=float(taksoS[2])
    sisse=float(taksoS[1])
    firma=taksoS[0]
    hind=sisse+(s*km)
    if hind <= odavaim_hind:
        odavaim_hind=hind
        odavaim_firma=firma
print(odavaim_firma)
f.close    
    
    