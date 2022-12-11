def sünnikuupäev(kood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    sajandi_kood = kood[0]
    aasta_kood = kood[1:3]
    if int(sajandi_kood) == 1 or int(sajandi_kood) == 2:
        aasta = "18" + aasta_kood
    elif int(sajandi_kood) == 3 or int(sajandi_kood) == 4:
        aasta = "19" + aasta_kood
    elif int(sajandi_kood) == 5 or int(sajandi_kood) == 6:
        aasta = "20" + aasta_kood
    else:
        aasta = "21" + aasta_kood
    kuu_kood = kood[3:5]
    kuu = kuud[(int(kuu_kood) - 1)]
    päev = kood[5:7]
    väljund = päev + ". " + kuu + " " + aasta
    return väljund