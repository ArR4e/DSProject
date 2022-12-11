

kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
numbrid = []
def sünnikuupäev(isikukood):
    for täht in isikukood:
        numbrid.append(täht)
        
    aasta = numbrid[1] + numbrid[2]
    if numbrid[3] == "0":
        kuu = int(numbrid[4]) - 1
    else:
        kuu = int(numbrid[3] + numbrid[4]) - 1
     
    if numbrid[5] == "0":
        päev = numbrid[6]
    else:
        päev = numbrid[5] + numbrid[6]
    
    kuu_sõnana = kuud[kuu]
    
    if numbrid[0] == "1" or numbrid[0] == "2":
        täisaasta = ("18" + aasta)
    elif numbrid[0] == "3" or numbrid[0] == "4":
        täisaasta = ("19" + aasta)
    else:
        täisaasta = ("20" + aasta)
        
    return (päev + ". " + str(kuu_sõnana) + " " + täisaasta)
