f=open("taksohinnad.txt", encoding="UTF-8")
kaugus=input(str("Sisesta kaugus koju "))
suur=1000000000
for rida in f:
    a=rida.split(",")
    starditasu=a[-2]
    kmtasu=a[-1]
    hind=float(starditasu)+(float(kmtasu)*float(kaugus))
    if kaugus==0:
        print("Pole valiidne")
    if suur>hind:
        suur=hind
        takso=a[-3]

print("Kõige odavam takso on", takso)

f.close()