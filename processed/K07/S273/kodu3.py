kuud = [0, "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(isikukood):
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        sünniaasta = 1800 + int(isikukood[1]) * 10 + int(isikukood[2])
    if int(isikukood[0]) == 4 or int(isikukood[0]) == 3:
        sünniaasta = 1900 + int(isikukood[1]) * 10 + int(isikukood[2])
    if int(isikukood[0]) == 6 or int(isikukood[0]) == 5:
        sünniaasta = 2000 + int(isikukood[1]) * 10 + int(isikukood[2])
    kuu = kuud[int(isikukood[3]) * 10 + int(isikukood[4])]
    päev = int(isikukood[5]) * 10 + int(isikukood[6])
    return str(päev) + ". " + str(kuu) + " " + str(sünniaasta)