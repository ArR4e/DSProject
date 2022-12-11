def odavaim_takso(teepikkus, taksohinnad):
    koik_hinnad=[]
    firma_nimed=[]

    #muutuv 
    a=0
    #Järjendite loomine
    while a<=(len(taksohinnad)-1):
        takso_hind=(float(taksohinnad[a][1])+(teepikkus*float(taksohinnad[a][2])))
        firma_nimed.append(taksohinnad[a][0])
        koik_hinnad.append(takso_hind)
        a+=1
    
    #odavaim
    if len(koik_hinnad)==0:
        print("Taksofirmasid ei ole")
    else:
        odavaim_hind=min(koik_hinnad)
        indeks=koik_hinnad.index(odavaim_hind)
        odavaim_takso=firma_nimed[indeks]
        print("Kõige odavam takso on " + str(odavaim_takso))
    
    
teepikkus=float(input("Sisestage teepikkus kilomeetrites: "))
    
fail=open("taksohinnad.txt","r",encoding="utf-8")
taksohinnad=[]
for rida in fail:
    rida=rida.rstrip("\n")
    element=rida.split(",")
    taksohinnad.append(element)


odavaim_takso(teepikkus, taksohinnad)