def sünnikuupäev(isikukood):
    sõne=isikukood
    kuud = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    aasta = sõne[1:3]
    kuu_nr = int(float(sõne[3:5]) -1)
    kuu = kuud[kuu_nr]
    päev = sõne[5:7]
    if sõne[0] == '1' or sõne[0] =='2':
        aastasada = '18'
    if sõne[0] == '3' or sõne[0] =='4':
        aastasada = '19'
    if sõne[0] == '5' or sõne[0] =='6':
        aastasada = '20'

    return päev+'. '+kuu+' '+aastasada+aasta