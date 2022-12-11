pikkus=float(input('Palun sisestage s6idu pikkus: '))
f=open('taksohinnad.txt')
odavaim=10000
nimi=''
for rida in f:
    a=rida.split(",",)
    hind=float(a[1])+pikkus*float(a[2])
    if hind<odavaim:
        nimi=a[0]
        odavaim=hind
print("Kõige odavam on "+nimi)