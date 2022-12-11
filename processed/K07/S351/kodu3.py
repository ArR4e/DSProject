def sünnikuupäev(isikukood):
    isikukoodi_numbrid=[]
    for element in isikukood:
        isikukoodi_numbrid.append(element)
    #päev
    paev=isikukoodi_numbrid[5]+isikukoodi_numbrid[6]
    #kuu nimi
    kuu=(isikukoodi_numbrid[3]+isikukoodi_numbrid[4])
    if kuu=="01":
        lõplik_kuu="jaanuar"
    elif kuu=="02":
        lõplik_kuu="veebruar"
    elif kuu=="03":
        lõplik_kuu="märts"
    elif kuu=="04":
        lõplik_kuu="aprill"
    elif kuu=="05":
        lõplik_kuu="mai"
    elif kuu=="06":
        lõplik_kuu="juuni"
    elif kuu=="07":
        lõplik_kuu="juuli"
    elif kuu=="08":
        lõplik_kuu="august"
    elif kuu=="09":
        lõplik_kuu="september"
    elif kuu=="10":
        lõplik_kuu="oktoober"
    elif kuu=="11":
        lõplik_kuu="november"
    else:
        lõplik_kuu="detsember"
    
    #aasta kaks viimast
    aasta_viimased=(isikukoodi_numbrid[1]+isikukoodi_numbrid[2])
    #aasta kaks esimest
    aasta_esimesed=int(isikukoodi_numbrid[0])
    if aasta_esimesed==1 or aasta_esimesed==2:
        esimesed_arvud=18
    elif aasta_esimesed==3 or aasta_esimesed==4:
        esimesed_arvud=19
    else:
        esimesed_arvud=20
    #lõplik aastaarv
    lõplik_aastaarv=str(esimesed_arvud)+str(aasta_viimased)
    #Lõplik vastus
    vastus=(str(paev) + ". " + lõplik_kuu + " "+ lõplik_aastaarv )
    return vastus
    
    
    
    
