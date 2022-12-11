def sünnikuupäev(kood):
    eraldi = []
    for i in kood:
        eraldi.append(i)
    aasta = ""
    kuu = eraldi[3] + eraldi[4]
    päev = eraldi[5] + eraldi[6]
    kuudenimed = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuudenumbrid = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    for i in kuudenumbrid:
        if i == kuu:
            i = int(i)
            kuu = kuudenimed[i-1]
    
    if eraldi[0] == "1" or eraldi[0] == "2":
        aasta += "18"
    elif eraldi[0] == "3" or eraldi[0] == "4":
        aasta += "19"
    elif eraldi[0] == "5" or eraldi[0] == "6":
        aasta += "20"
        
    return(päev + ". " + kuu + " " + aasta + eraldi[1] + eraldi[2])
print(sünnikuupäev("51106302810"))