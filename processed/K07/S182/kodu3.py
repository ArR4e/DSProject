def sünnikuupäev(isikukood):
    if isikukood[0]=="3" or isikukood[0]=="4":
        aasta="19"+isikukood[1:3]
    else:
        aasta="20"+isikukood[1:3]
    if isikukood[3:5]=="01":
        kuu="jaanuar"
    elif isikukood[3:5]=="02":
        kuu="veebruar"
    elif isikukood[3:5]=="03":
        kuu="märts"
    elif isikukood[3:5]=="04":
        kuu="aprill"
    elif isikukood[3:5]=="05":
        kuu="mai"
    elif isikukood[3:5]=="06":
        kuu="juuni"
    elif isikukood[3:5]=="07":
        kuu="juuli"
    elif isikukood[3:5]=="08":
        kuu="august"
    elif isikukood[3:5]=="09":
        kuu="september"
    elif isikukood[3:5]=="10":
        kuu="oktoober"
    elif isikukood[3:5]=="11":
        kuu="november"
    else:
        kuu="detsember"
    sünd=isikukood[5:7]+". "+kuu+" "+aasta
    return(sünd)

