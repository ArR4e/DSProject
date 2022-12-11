def sünnikuupäev(isikukood):
    kuupäev = ""
    kuud = ["01","jaanuar","02","veebruar","03","märts","04","aprill","05","mai","06","juuni","07","juuli","08","august","09","september","10","oktoober","11","november","12","detsember"]
    
    if isikukood[0] in ["1","2"]:
        kuupäev += "18"
    elif isikukood[0] in ["3","4"]:
        kuupäev += "19"
    elif isikukood[0] in ["5","6"]:
        kuupäev += "20"
        
    kuupäev += str(isikukood[1:3])
    
    kuu = isikukood[3:5]
    kuu_asukoht = kuud.index(kuu)
    
    kuupäev = kuud[kuu_asukoht + 1] + " " + kuupäev
    
    kuupäev = isikukood[5:7] + ". " + kuupäev
    
    return kuupäev
    
print(sünnikuupäev('50107132740')  )