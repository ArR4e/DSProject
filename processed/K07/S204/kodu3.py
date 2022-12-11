isikukood = str(input("Sisesta oma isikukood: "))

def sünnikuupäev(isikukood):

    kuupäev = isikukood[5:7]
    kuun = isikukood[3:5]
    kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if kuun == "01":
        kuu = kuude_järjend[0]
    if kuun == "02":
        kuu = kuude_järjend[1]
    if kuun == "03":
        kuu = kuude_järjend[2]
    if kuun == "04":
        kuu = kuude_järjend[3]
    if kuun == "05":
        kuu = kuude_järjend[4]
    if kuun == "06":
        kuu = kuude_järjend[5]
    if kuun == "07":
        kuu = kuude_järjend[6]
    if kuun == "08":
        kuu = kuude_järjend[7]
    if kuun == "09":
        kuu = kuude_järjend[8]
    if kuun == "10":
        kuu = kuude_järjend[9]
    if kuun == "11":
        kuu = kuude_järjend[10]
    if kuun == "12":
        kuu = kuude_järjend[11]
        
        
    if isikukood[0] == "1" or isikukood [0] == "2":
        aasta = "18"+ isikukood[1:3]
        sünnikuuppäev = kuupäev + ". " + kuu + " " + aasta
        return sünnikuuppäev
    if isikukood[0] == "3" or isikukood [0] == "4":
        aasta = "19"+ isikukood[1:3]
        sünnikuuppäev = kuupäev + ". " + kuu + " " + aasta
        return sünnikuuppäev
    if isikukood[0] == "5" or isikukood [0] == "6":
        aasta = "20"+ isikukood[1:3]
        sünnikuuppäev = kuupäev + ". " + kuu + " " + aasta
        return sünnikuuppäev
    

    
print(sünnikuupäev(isikukood))


    
         
    
    