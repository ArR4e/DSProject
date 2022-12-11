file=open("taksohinnad.txt",encoding="UTF-8")
tee=float(input("Sisestage kilomeetrite hind: "))
a=[]
sisse=0
km=0
nimi=""
kokku=0
väikseim=0
for rida in file:
    a=rida.split(",")
    sisse= a[1]
    km=a[2]
    kokku=float(sisse)+tee*float(km)
    if kokku<väikseim or väikseim==0:
        nimi=a[0]
        väikseim=kokku
        
print("Kõige odavam on "+str(nimi))
file.close()