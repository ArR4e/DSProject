def sünnikuupäev(isikukood):
    järjend = list(isikukood)
    
    if järjend[0] == "1" or järjend[0] == "2":
        aasta = str(int(järjend[1] + järjend[2]) + 1800)
    elif järjend[0] == "3" or järjend[0] == "4":
        aasta = str(int(järjend[1] + järjend[2]) + 1900)
    elif järjend[0] == "5" or järjend[0] == "6":
        aasta = str(int(järjend[1] + järjend[2]) + 2000)
        
    päev = str(järjend[5] + järjend[6]) + ". "
        
    if järjend[3] + järjend[4] == "01":
        kuupäev = "jaanuar "
    elif järjend[3] + järjend[4] == "02":
        kuupäev = "veebruar "
    elif järjend[3] + järjend[4] == "03":
        kuupäev = "märts "
    elif järjend[3] + järjend[4] == "04":
        kuupäev = "aprill "
    elif järjend[3] + järjend[4] == "05":
        kuupäev = "mai "
    elif järjend[3] + järjend[4] == "06":
        kuupäev = "juuni "
    elif järjend[3] + järjend[4] == "07":
        kuupäev = "juuli "
    elif järjend[3] + järjend[4] == "08":
        kuupäev = "august "
    elif järjend[3] + järjend[4] == "09":
        kuupäev = "september "
    elif järjend[3] + järjend[4] == "10":
        kuupäev = "oktoober "
    elif järjend[3] + järjend[4] == "11":
        kuupäev = "november "
    elif järjend[3] + järjend[4] == "12":
        kuupäev = "detsember "
    
    return päev + kuupäev + aasta
   
  