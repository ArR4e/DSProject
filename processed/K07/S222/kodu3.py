def sünnikuupäev(a):
    skp = ""
    skp += a[5:7]
    skp += ". "
    kuu = a[3:5]
    if kuu == "01":
        skp += "jaanuar "
    elif kuu == "02":
        skp += "veebruar "
    elif kuu == "03":
        skp += "märts "
    elif kuu == "04":
        skp += "aprill "
    elif kuu == "05":
        skp += "mai "
    elif kuu == "06":
        skp += "juuni "
    elif kuu == "07":
        skp += "juuli "
    elif kuu == "08":
        skp += "august "
    elif kuu == "09":
        skp += "september "
    elif kuu == "10":
        skp += "oktoober "
    elif kuu == "11":
        skp += "november "
    elif kuu == "12":
        skp += "detsember "
    
    if a[0] == "3" or a[0] == "4":
        skp += "19"
    elif a[0] == "5" or a[0] == "6":
        skp += "20"
    
    skp += a[1:3]
        
    return skp
    
print(sünnikuupäev("34501234215"))