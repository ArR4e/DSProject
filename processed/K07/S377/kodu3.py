#sünnikuupäevad
#mirjampirn

def sünnikuupäev(isikukood):
    päev_nr=isikukood[5:7]
    if päev_nr[0]=="0":
        päev=päev_nr[1:]
    else:
        päev=päev_nr
    kuu_nr=isikukood[3:5]
    if kuu_nr=="01":
        kuu="jaanuar"
    elif kuu_nr=="02":
        kuu="veebruar"
    elif kuu_nr=="03":
        kuu="märts"
    elif kuu_nr=="04":
        kuu="aprill"
    elif kuu_nr=="05":
        kuu="mai"
    elif kuu_nr=="06":
        kuu="juuni"
    elif kuu_nr=="07":
        kuu="juuli"
    elif kuu_nr=="08":
        kuu="august"
    elif kuu_nr=="09":
        kuu="september"
    elif kuu_nr=="10":
        kuu="oktoober"
    elif kuu_nr=="11":
        kuu="november"
    elif kuu_nr=="12":
        kuu="detsember"
    aastaarv=isikukood[1:3]
    sajand=isikukood[0:1]
    if sajand=="1" or sajand=="2":
        sajand_nr="18"
    elif sajand=="3" or sajand=="4":
        sajand_nr="19"
    elif sajand=="5" or sajand=="6":
        sajand_nr="20"
    aasta=sajand_nr+aastaarv
    print(päev,kuu_nr,aastaarv,sajand)
    synnikuupäev=päev+". "+kuu+" "+aasta
    return synnikuupäev
    
