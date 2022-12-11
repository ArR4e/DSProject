

def sünnikuupäev(ik):
    
    isikukood = list(ik)
    aasta = isikukood[1:3]
    aasta = ''.join(aasta)
    
    if(isikukood[0] =='1' or isikukood[0] =='2'):
        aasta = '18' + aasta
    elif(isikukood[0] =='3' or isikukood[0] =='4'):
        aasta = '19' + aasta
    else:
        aasta = '20' + aasta    
    
    
    kuu = isikukood[3:5]
    kuu = ''.join(kuu)
    if kuu  == "01":
        kuu = "jaanuar"
    elif kuu  == "02":
        kuu = "veebruar"
    elif kuu  == "03":
        kuu = "märts"
    elif kuu  == "04":
        kuu = "aprill"
    elif kuu  == "05":
        kuu = "mai"
    elif kuu  == "06":
        kuu = "juuni"
    elif kuu  == "07":
        kuu = "juuli"
    elif kuu  == "08":
        kuu = "august"
    elif kuu  == "09":
        kuu = "september"
    elif kuu  == "10":
        kuu = "oktoober"
    elif kuu  == "11":
        kuu = "november"
    else:
        kuu = "detsember"
        
    isikukood = list(ik)
    kp = isikukood[5:7]
    kp = ''.join(kp)
    
    return(kp + ". " + kuu + " " + aasta)
    

    
sünnikuupäev('49111084219')

