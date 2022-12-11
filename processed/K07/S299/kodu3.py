kuud=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
def sünnikuupäev(isikukood):
    päev=isikukood[5:7]
    kuu=kuud[int(isikukood[3:5])-1]
    if int(isikukood[0])<3:
      aasta='18'+isikukood[1:3]
    elif int(isikukood[0])<5:
        aasta='19'+isikukood[1:3]
    elif int(isikukood[0])<7:
        aasta='20'+isikukood[1:3]
    sünnikuupäev= päev +'. ' + kuu + ' ' + aasta
    return sünnikuupäev