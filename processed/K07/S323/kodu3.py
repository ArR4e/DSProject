kood = 50010260847
def sünnikuupäev(kp):
    kp = str(kp)
    aasta = kp[1:3]
    kuu =kp[3:5]
    päev = kp[5:7]
    
    if päev[0] == "0":
        päev = kp[6:7]
    
    if kuu == "01":
        sünnikuu = "jaanuar"
    if kuu == "02":
        sünnikuu = "veebruar"
    if kuu == "03":
        sünnikuu = "märts"
    if kuu == "04":
        sünnikuu = "aprill"
    if kuu == "05":
        sünnikuu = "main"
    if kuu == "06":
        sünnikuu = "juuni"
    if kuu == "07":
        sünnikuu = "juuli"
    if kuu == "08":
        sünnikuu = "august"
    if kuu == "09":
        sünnikuu = "september"
    if kuu == "10":
        sünnikuu = "oktoober"
    if kuu == "11":
        sünnikuu = "november"
    if kuu == "12":
        sünnikuu = "detsember"
        
    sünnipäev = päev + ". " + sünnikuu + " " + str(19) +  aasta 
    return sünnipäev
    
print(sünnikuupäev(kood))