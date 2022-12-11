def sünnikuupäev (isikukood):
    sõne = ""
    
    if isikukood[5] == "0":
        sõne += isikukood[6] + ". "
    
    else:
        sõne += isikukood[5:7] + ". "
    
    if isikukood[3:5] == "01":
        sõne += "jaanuar"
    
    elif isikukood[3:5] == "02":
        sõne += "veebruar"
        
    elif isikukood[3:5] == "03":
        sõne += "märts"
        
    elif isikukood[3:5] == "04":
        sõne += "aprill"
        
    elif isikukood[3:5] == "05":
        sõne += "mai"
        
    elif isikukood[3:5] == "06":
        sõne += "juuni"
        
    elif isikukood[3:5] == "07":
        sõne += "juuli"
        
    elif isikukood[3:5] == "08":
        sõne += "august"
        
    elif isikukood[3:5] == "09":
        sõne += "september"
        
    elif isikukood[3:5] == "10":
        sõne += "oktoober"
        
    elif isikukood[3:5] == "11":
        sõne += "november"
        
    elif isikukood[3:5] == "12":
        sõne += "detsember"
        
    if int (isikukood[0]) < 3:
        sõne += " 18" + isikukood[1:3]
    
    elif int (isikukood[0]) < 5:
        sõne += " 19" + isikukood[1:3]
    
    elif int (isikukood[0]) < 7:
        sõne += " 20" + isikukood[1:3]
    
    else:
        sõne += " 21" + isikukood[1:3]
    
    return sõne

print (sünnikuupäev ('34501234215'))