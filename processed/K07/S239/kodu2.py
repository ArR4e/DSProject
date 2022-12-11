f=open("taksohinnad.txt",encoding="UTF-8")
s=float(input("Mitu km sõidate? "))
i=999999999999
valik=("nautida hetke")
for rida in f:
    a=rida.split(",")
    takso=a[0]
    alghind=float(a[1])
    km_hind=float(a[2])
    if s*km_hind+alghind<i:
        valik=a[0]
    i=s*km_hind+alghind
f.close()

print("Odavaim valik oleks",valik)