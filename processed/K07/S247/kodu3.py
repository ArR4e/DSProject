# 60202170229
def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuupäev = isikukood[5:7]
    kuu = int(isikukood[3:5])
    aasta = "20" +  isikukood[1:3]
    print(kuupäev + ".",kuud[kuu-1], aasta)
    
sünnikuupäev("60202170229")
    

    
    
        
    
    