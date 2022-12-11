def sünnikuupäev(isikukood):
    kuud = ['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    aastad = ['18','19','20','21']
    jupid = isikukood
    sajand = int(jupid[0])
    lõpp = jupid[1:3]
    if sajand == 1 or sajand == 2:
        aasta = aastad[0]
    if sajand == 3 or sajand == 4:
        aasta = aastad[1]
    if sajand == 5 or sajand == 6:
        aasta = aastad[2]
    if sajand == 7 or sajand == 8:
        aasta = aastad[3]
    kuu = jupid[3:5]
    if int(kuu) < 10:
       kuu = kuu.replace("0", "")
    päev = jupid[5:7]
    aastaaeg = kuud[int(kuu)-1]
    kuupäev = "{}. {} {}".format(päev, aastaaeg, aasta + lõpp)
    return kuupäev

isikukood = "60009050249"
print(sünnikuupäev(isikukood))
    
