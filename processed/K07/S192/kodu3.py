kuud = ['', 'jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
def sünnikuupäev(isikukood):
    i = list(isikukood)
    sajand = ''.join(i[0])
    aasta_nr = ''.join(i[1:3])
    if sajand in ['1', '2']:
        aasta = '18' + aasta_nr
    elif sajand in ['3', '4']:
        aasta = '19' + aasta_nr
    elif sajand in ['5', '6']:
        aasta = '20' + aasta_nr
    kuu_number = int(''.join(i[3:5]))
    kuu = kuud[kuu_number]
    kuupäev = ''.join(i[5:7])
    return(kuupäev + '. ' + kuu + ' ' + aasta)

    