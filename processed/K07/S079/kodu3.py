# 3. Sünnikuupäev isikukoodist
# Kirjuta funktsioon sünnikuupäev, mis võtab argumendiks Eesti isikukoodi sõnena ning tagastab
# sünnikuupäeva kujul <päev>. <kuu nimi> <aasta>.

# Näide
# >>> sünnikuupäev('34501234215')
# '23. jaanuar 1945'
# Automaatkontroll. Funktsioon peab olema sünnikuupäev (täpitähtedega), ühe argumendiga. Nii argument kui ka funktsiooni
# tagastatav väärtus on sõned. Põhiprogramm võib seda funktsiooni kasutada ja sooritada sisend-väljundoperatsioone,
# aga automaatkontroll testib ainult funktsiooni sünnikuupäev. Funktsiooni tagastatavas väärtuses peavad kuude
# nimed olema täpitähtedega, nt märts. Kuupäeva numbri ja kuu nime vahel peab olema üks tühik.
# Seega 21. märts, mitte 21.märts. Samuti peab olema täpselt üks tühik kuu nime ja aastaarvu vahel.

def sünnikuupäev(isikukood):
    
    sünniaasta = str(isikukood)[1:3]
    sünnikuu = str(isikukood)[3:5]
    päev = str(isikukood)[5:7]
    
    # teeme aastad korda
    if str(isikukood)[0] == "1" or str(isikukood)[0] == "2":
        aasta = "18" + sünniaasta
    elif  str(isikukood)[0] == "3" or str(isikukood)[0] == "4":
        aasta = "19" + sünniaasta
    elif  str(isikukood)[0] == "5" or str(isikukood)[0] == "6":
        aasta = "20" + sünniaasta
    
      # kuud
    if sünnikuu == "01":
        kuu = "jaanuar"
    elif sünnikuu == "02":
        kuu = "veebruar"
    elif sünnikuu == "03":
        kuu = "märts"
    elif sünnikuu == "04":
        kuu = "aprill"
    elif sünnikuu == "05":
        kuu = "mai"
    elif sünnikuu == "06":
        kuu = "juuni"
    elif sünnikuu == "07":
        kuu = "juuli"
    elif sünnikuu == "08":
        kuu = "august"
    elif sünnikuu == "09":
        kuu = "september"
    elif sünnikuu == "10":
        kuu = "oktoober"
    elif sünnikuu == "11":
        kuu = "november"
    elif sünnikuu == "12":
        kuu = "detsember"
        
    return str(päev) + ". " + kuu + " " + aasta
        
        
    
