def sünnikuupäev(a):
    kuu_nr=a[3:5]
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
    else:
        print("See pole isikukood")
        
    päev=a[5:7]
    aasta=a[1:3]
    if a[0]=="1" or a[0]=="2":
        aasta="18"+aasta
    elif a[0]=="3" or a[0]=="4":
        aasta="19"+aasta
    elif a[0]=="5" or a[0]=="6":
        aasta="20"+aasta
    elif a[0]=="7" or a[0]=="8":
        aasta="21"+aasta
        
    vastus=str(päev)+". "+kuu+" "+aasta
    return vastus
a="60012242762"
sünnikuupäev(a)