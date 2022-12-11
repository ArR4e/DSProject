def sünnikuupäev(isikukood):
    järjend = []
    kuu = 0
    for i in isikukood:
        järjend.append(i)
    if järjend[0] == "1" or järjend[0] == "2": 
        aasta = "18" + järjend[1] + järjend[2]
    elif järjend[0] == "3" or järjend[0] == "4":
        aasta = "19" + järjend[1] + järjend[2]
    elif järjend[0] == "5" or järjend[0] == "6":
        aasta = "20" + järjend[1] + järjend[2]
    elif järjend[0] == "7" or järjend[0] == "8":
        aasta = "21" + järjend[1] + järjend[2]
        
        
    if järjend[3] + järjend[4] == "01":
        kuu = "jaanuar"
    elif järjend[3] + järjend[4] == "02":
        kuu = "veebruar"
    elif järjend[3] + järjend[4] == "03":
        kuu = "märts"
    elif järjend[3] + järjend[4] == "04":
        kuu = "aprill"
    elif järjend[3] + järjend[4] == "05":
        kuu = "mai"
    elif järjend[3] + järjend[4] == "06":
        kuu = "juuni"
    elif järjend[3] + järjend[4] == "07":
        kuu = "juuli"
    elif järjend[3] + järjend[4] == "08":
        kuu = "august"
    elif järjend[3] + järjend[4] == "09":
        kuu = "september"
    elif järjend[3] + järjend[4] == "10":
        kuu = "oktoober"
    elif järjend[3] + järjend[4] == "11":
        kuu = "november"
    elif järjend[3] + järjend[4] == "12":
        kuu = "detsember"
    
    kuupäev = järjend[5] + järjend[6]
    
    return (kuupäev + "." + " " + kuu + " " + aasta)
    
