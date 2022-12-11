def sünnikuupäev(isikukood):
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    päev = isikukood[5:7]
    kuu_arv = int(isikukood[3:5])
    kuu_sõne = kuud[kuu_arv - 1]
    if isikukood[0]== str(1) or isikukood[0]==str(2):
        aasta_algus = str(18)
    elif isikukood[0]== str(3) or isikukood[0]== str(4):
        aasta_algus = str(19)
    else:
        aasta_algus = str(20)
    aasta = aasta_algus + isikukood[1:3]
    sünnikuupäev = päev +". " + kuu_sõne + " " + aasta
    return(sünnikuupäev)