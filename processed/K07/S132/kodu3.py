def sünnikuupäev(ID):
    kuud = {"01":"jaanuar",
            "02":"veebruar",
            "03":"märts",
            "04":"aprill",
            "05":"mai",
            "06":"juuni",
            "07":"juuli",
            "08":"august",
            "09":"september",
            "10":"oktoober",
            "11":"november",
            "12":"detsember",}
    s_n = ID[1:7]
    sajand = ID[0]
    aasta = s_n[0] + s_n[1]
    kuu = s_n[2] + s_n[3]
    paev = s_n[4] + s_n[5]
    if sajand == "5" or sajand == "6":
        kuupaev = paev + '. ' + kuud[kuu] + ' ' + '20' + aasta
    elif sajand == "3" or sajand == "4":
        kuupaev = paev + '. ' + kuud[kuu] + ' ' + '19' + aasta
    elif sajand == "1" or sajand == "2":
        kuupaev = paev + '. ' + kuud[kuu] + ' ' + '18' + aasta
    return kuupaev