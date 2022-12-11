def sünnikuupäev(isikukood):
    kuupäev = str(ikood)[5:7]
    kuu = str(ikood)[3:5]
    aasta = str(ikood)[1:3]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "juuni", "august",
            "september", "oktoober", "november", "detsember"]
    if int(aasta) < 100 and int(aasta) > 22:
        aasta = "19" +aasta
    else:
        aasta = "20" + aasta
    
    print(kuupäev + "." + kuud[int(kuu)-1], aasta)
    
    
ikood= int(input("Sisesta isikukood: "))
sünnikuupäev(ikood)