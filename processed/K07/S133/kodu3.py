def sünnikuupäev(isikukood):
    kuu_number=isikukood[3:5]
    if kuu_number == "01":
        kuu="jaanuar"
    elif kuu_number == "02":
        kuu="veebruar"
    elif kuu_number == "03":
        kuu="märts"
    elif kuu_number == "04":
        kuu="aprill"
    elif kuu_number == "05":
        kuu="mai"
    elif kuu_number == "06":
        kuu="juuni"
    elif kuu_number == "07":
        kuu="juuli"
    elif kuu_number == "08":
        kuu="august"
    elif kuu_number == "09":
        kuu="september"
    elif kuu_number == "10":
        kuu="oktoober"
    elif kuu_number == "11":
        kuu="november"
    elif kuu_number == "12":
        kuu="detsember"
    kuupäev=isikukood[5:7]
    sajand=isikukood[0]
    if sajand =="1" or sajand=="2":
        aasta_algus="18"
    elif sajand == "3" or sajand=="4":
        aasta_algus="19"
    elif sajand =="5" or sajand=="6":
        aasta_algus="20"
    e=(str(kuupäev) + ". " + str(kuu)+ " " + str(aasta_algus)+str(isikukood[1:3]))
    return e