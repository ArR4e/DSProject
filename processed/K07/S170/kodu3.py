def sünnikuupäev(x):
    aas = x [0]
    if  aas == "1" or aas == "2":
        aas = 18
    elif aas == "3" or aas == "4":
        aas = 19
    elif aas == "5" or aas == "6":
        aas = 20
    sta = x [1:3]
    aasta = str(aas) + str(sta)
    
    kuu = x [3:5]
    if kuu == "01":
        kuu = "jaanuar"
    elif kuu == "02":
        kuu = "veebruar"
    elif kuu == "03":
        kuu = "märts"
    elif kuu == "04":
        kuu = "aprill"
    elif kuu == "05":
        kuu = "mai"
    elif kuu == "06":
        kuu = "juuni"
    elif kuu == "07":
        kuu = "juuli"
    elif kuu == "08":
        kuu = "august"
    elif kuu == "09":
        kuu = "september"
    elif kuu == "10":
        kuu = "oktoober"
    elif kuu == "11":
        kuu = "november"
    elif kuu == "12":
        kuu = "detsember"
        
    päev = x [5:7]
    return (str(päev + ". " + kuu + " " + aasta))
    
    
print(sünnikuupäev("60101017683"))