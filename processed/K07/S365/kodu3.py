kood = str(input("kirjuta oma isikukood : "))

def sünnikuupäev(kood):
    päev = kood[5:7]
    kuu = kood[3:5]
    aasta = kood[1:3]
    if kuu == "01":
        kuu = "jaanuar"
    if kuu == "02":
        kuu = "veebruar"
    if kuu == "03":
        kuu = "märts"
    if kuu == "04":
        kuu = "aprill"
    if kuu == "05":
        kuu = "mai"
    if kuu == "06":
        kuu = "juuni"
    if kuu == "07":
        kuu = "juuli"
    if kuu == "08":
        kuu = "august"
    if kuu == "09":
        kuu = "september"
    if kuu == "10":
        kuu = "oktoober"
    if kuu == "11":
        kuu = "november"
    if kuu == "12":
        kuu = "detsember"
    if kood[0] == "1" or kood[0] == "2":
        aasta = "18"+aasta
    if kood[0] == "3" or kood[0] == "4":
        aasta = "19"+aasta
    if kood[0] == "5" or kood[0] == "6":
        aasta ="20"+aasta
    sünnipäev =(päev+"."+" "+kuu+" "+aasta)
    return sünnipäev

print(sünnikuupäev(kood))