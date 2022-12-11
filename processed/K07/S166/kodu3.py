#sünnikuupäev("50107261418")
#sünnikuupäev("38010307777")
def sünnikuupäev(isikukood):
    isikukood=list(isikukood)
    sajand = int(isikukood[0])
    if sajand==1 or sajand==2:
        sajand='18'
    elif sajand ==3 or sajand==4:
        sajand='19'
    elif sajand == 5 or sajand== 6:
        sajand ='20'
    elif sajand == 7 or sajand == 8:
        sajand='21'
    aasta=isikukood[1]+isikukood[2]
    kuu=int(isikukood[3]+isikukood[4])
    kuud=['niisama','jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu=kuud[kuu]
    päev=isikukood[5]+isikukood[6]
    return päev+'. '+kuu+' '+sajand+aasta