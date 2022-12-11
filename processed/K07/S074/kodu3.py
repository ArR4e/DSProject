#Isikukoodi sisestamine
isikukood = input("Sisesta siia oma isikukood: ")
#Kuude list
kuud = ["jaanuar" , "veebruar" , "märts" , "aprill" , "mai" , "juuni" , "juuli",
        "august" , "september" , "oktoober" , "november" , "detsember"]
#Sünnikuupäev funktsioon
def sünnikuupäev(isikukood):
    #Aasta määramine
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2 :
        aasta = "18" + str(isikukood[1] + isikukood[2])
    elif int(isikukood[0]) == 3 or int(isikukood[0]) == 4 :
        aasta = "19" + str(isikukood[1] + isikukood[2])
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6 :
        aasta = "20" + str(isikukood[1] + isikukood[2])
    elif int(isikukood[0]) == 7 or int(isikukood[0]) == 8 :
        aasta = "21" + str(isikukood[1] + isikukood[2])
    #Kuu nime määramine
    for kuunimi in kuud :
        kuu = int(isikukood[3] + isikukood[4])
        kuunimi = kuud[kuu-1]
        
    #Päeva määramine isikukoodist
    päev = int(isikukood[5] + isikukood[6])
    if päev >= 1 or päev <= 31:
        sünnikuupäev1 = str(päev) + ". " + str(kuunimi) + " " + str(aasta)
    return sünnikuupäev1
    
print(sünnikuupäev(isikukood))