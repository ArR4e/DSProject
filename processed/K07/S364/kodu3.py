def sünnikuupäev(kood):
    months = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    päev = kood[5:7]
    kuu = kood[3:5]
    aasta = kood[1:3]
    kuu = int(kuu)-1
    
    if kood[0] == "1" or kood[0] == "2":
        return(päev + '. ' + months[kuu] + ' ' + "18" + aasta)
    elif kood[0] == "3" or kood[0] == "4":
        return(päev + '. ' + months[kuu] + ' ' + "19" + aasta)
    elif kood[0] == "5" or kood[0] == "6":
        return(päev + '. ' + months[kuu] + ' ' + "20" + aasta)
    elif kood[0] == "7" or kood[0] == "8":
        return(päev + '. ' + months[kuu] + ' ' + "21" + aasta)
    
print(sünnikuupäev("50206273746"))
    
    
    