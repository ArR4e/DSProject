
def sünnikuupäev(isikukood):
    järjend = list(isikukood)
    
    aasta_järjend = järjend[1:3]
    aasta = "".join(aasta_järjend)
    esimene_number = järjend[0]
    if esimene_number == "1" or esimene_number == "2":
        aasta = "18" + aasta
        
    elif esimene_number == "3" or esimene_number == "4":
        aasta = "19" + aasta
    elif esimene_number == "5" or esimene_number == "6":
        aasta = "20" + aasta
    elif esimene_number == "7" or esimene_number == "8":
        aasta = "21" + aasta
    kuu_järjend = järjend[3:5]
    kuu = "".join(kuu_järjend)
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
    päev_järjend = järjend[5:7]
    päev = "".join(päev_järjend)
    
    vastus = päev + ". " + kuu + " " + aasta
    
    return vastus
    
    

print(sünnikuupäev("34501234215"))
