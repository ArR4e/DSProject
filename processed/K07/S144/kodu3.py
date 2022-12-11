import datetime
import locale
locale.setlocale(locale.LC_TIME, "et_EE")
def sünnikuupäev(a):
    kuu = a[3:5]
    kuu = int(kuu)
    kuu = datetime.date(1900, kuu , 1).strftime('%B')
    päev = a[5:7]
    päev = päev.strip('0')
    aastakood = a[0:3]
    if aastakood[0] == '1':
        aasta = 1800 + int(aastakood[1:3])
    elif aastakood[0] == '3' or aastakood[0] == '4':
        aasta = 1900 + int(aastakood[1:3])
    elif aastakood[0] == '5' or aastakood[0] == '6':
        aasta = 2000 + int(aastakood[1:3])
    print(f'{päev}. {kuu} {aasta}')
        
