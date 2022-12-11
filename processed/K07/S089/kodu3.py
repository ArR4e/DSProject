def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    aasta = isikukood[1:3]
    kuude_järjend = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu_nimega = kuude_järjend[(int(kuu)-1)]
    return(str(päev + '. ' + kuu_nimega + ' 19' +aasta))