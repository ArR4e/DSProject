kuud = ["jaanuar", 'veebruar', 'märts', "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(kood):
    aasta = ''
    kuu = ''
    päev = ''
    if kood[0] == "1" or kood[0] == "2":
        aasta += '18'
    if kood[0] == "3" or kood[0] == "4":
        aasta += '19'
    if kood[0] == "5" or kood[0] == "6":
        aasta += '20'
    aasta += kood[1] + kood[2]
    kuu = kuud[int(kood[3:5])-1]
    päev = kood[5:7]
    lopp = päev + '. ' + kuu + ' ' + aasta
    return lopp