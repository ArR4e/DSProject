pikkus=float(input("Sisesta tee pikkus kilomeetrites: "))
fail=open("taksohinnad.txt", encoding="UTF-8")
taksod=[]
for rida in fail:
    x=rida.strip()
    y=x.split(',')
    taksod.append(y)
fail.close()
odavaim=[]
for rida in taksod:
    hind=pikkus*float(rida[2])+float(rida[1])
    odavaim.append(hind)
print("Odavaim takso on " + str(taksod[odavaim.index(min(odavaim))][0]))