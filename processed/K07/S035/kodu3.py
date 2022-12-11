def sünnikuupäev(isikukood):
    isikukood=list(isikukood)
    b= (isikukood[1] + isikukood[2])
    if (isikukood[3] + isikukood[4])=="01":
        c="jaanuar"
    if (isikukood[3] + isikukood[4])=="02":
        c="veebruar"
    if (isikukood[3] + isikukood[4])=="03":
        c="märts"
    if (isikukood[3] + isikukood[4])=="04":
        c="aprill"
    if (isikukood[3] + isikukood[4])=="05":
        c="mai"
    if (isikukood[3] + isikukood[4])=="06":
        c="juuni"
    if (isikukood[3] + isikukood[4])=="07":
        c="juuli"
    if (isikukood[3] + isikukood[4])=="08":
        c="august"
    if (isikukood[3] + isikukood[4])=="09":
        c="september"
    if (isikukood[3] + isikukood[4])=="10":
        c="oktoober"
    if (isikukood[3] + isikukood[4])=="11":
        c="november"
    if (isikukood[3] + isikukood[4])=="12":
        c="detsember"
    d=(isikukood[5] + isikukood [6])
    if isikukood[0]=="3" or isikukood[0]=="4":
        a=19
    if isikukood[0]=="5" or isikukood[0]=="6":
        a=20
    if isikukood[0]=="1" or isikukood[0]=="2":
        a=18
    return (str(d)+". " + str(c) + " " + str(a)+str(b))

    

        