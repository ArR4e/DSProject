# Sünnikuupäev isikukoodist

def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli",
            "august", "september", "oktoober","november", "detsember"]
    kuupäev = isikukood[:7]
    if int(kuupäev[3:5]) < 10:
        kuu = kuud[int(kuupäev[4])-1]
    elif int(kuupäev[3:5]) >= 10 and int(kuupäev[3:5]) <= 12:
        kuu = kuud[int(kuupäev[3:5])-1]
    if int(kuupäev[0]) == 1 or int(kuupäev[0]) == 2:
        aasta = " 18" + kuupäev[1:3]
    elif int(kuupäev[0]) == 3 or int(kuupäev[0]) == 4:
        aasta = " 19" + kuupäev[1:3]
    elif int(kuupäev[0]) == 5 or int(kuupäev[0]) == 6:
        aasta = " 20" + kuupäev[1:3]
    
    return (kuupäev[-2:] + ". " + kuu + aasta)

print(sünnikuupäev('60101017683'))