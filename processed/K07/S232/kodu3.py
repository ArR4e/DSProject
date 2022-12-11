kuud = {"01": "jaanuar", "02": "veebruar", "03": "märts", "04": "aprill", "05": "mai", "06": "juuni", "07": "juuli", \
        "08": "august", "09": "september", "10": "oktoober", "11": "november", "12": "detsember"}

def sünnikuupäev(isikukood):
    isikukood = str(isikukood)
    sajand = isikukood[0]
    aasta = isikukood[1:3]
    kuu = isikukood[3:5]
    päev = isikukood[5:7]
    
    kuu = kuud[kuu]
    if sajand == "5" or sajand == "6":
        aasta = "20" + aasta
    elif sajand == "3" or sajand == "4":
        aasta = "19" + aasta
    elif sajand == "1" or sajand == "2":
        aasta = "18" + aasta
    
    return "{0}. {1} {2}".format(päev, kuu, aasta)

sünnikuupäev(34501234215)