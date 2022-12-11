def sünnikuupäev (isikukood):
    if len(isikukood) == 11:
            if isikukood [0] in ('3', '4'):
                aasta = 1900
            elif isikukood [0] in ('5','6'):
                aasta = 2000
            else:
                aasta = 1800
            kümnend = int(isikukood[1:3])
            aasta += kümnend
            kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai','juuni', 'juuli', 'august','september','oktoober','november', 'detsember']
            kuu = int(isikukood[3:5])
            päev = int(isikukood[5:7])
            ik_sõnena = str(päev) + ". " + kuud[kuu-1] + " " + str(aasta)
    return ik_sõnena
print(sünnikuupäev('19907062285'))