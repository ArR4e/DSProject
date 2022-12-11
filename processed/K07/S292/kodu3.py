def sünnikuupäev(kood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli",
        "august", "september", "oktoober", "november", "detsember"]

    aasta = kood[1]+kood[2]
    kuu = kuud[int(kood[3]+kood[4])-1]
    päev = kood[5]+kood[6]
    if kood[0] == "1" or kood[0] == "2":
        synna = päev + ". "+ kuu + " 18"+aasta
    elif kood[0] == "3" or kood[0] == "4":
        synna = päev + ". "+ kuu + " 19"+aasta
    else:
        synna = päev + ". "+ kuu + " 20"+aasta
    return synna