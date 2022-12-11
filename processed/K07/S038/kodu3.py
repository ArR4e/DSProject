kood = str(input("Sisestage isikukood: "))
def sünnikuupäev(a):
    sajand = int(kood[0])
    if 0 < sajand < 3:
        aasta = "18"+ str(kood[1])+ str(kood[2])
    elif 2 < sajand < 5:
        aasta = "19"+ str(kood[1])+ str(kood[2])
    else:
        aasta = "20"+ str(kood[1])+ str(kood[2])    
    kuunr = str(kood[3])+str(kood[4])
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuu = kuud[int(kuunr)-1]
    p2ev = str(kood[5]) + str(kood[6])
    
    return (p2ev+". "+kuu+" "+aasta)

sünnikuupäev(kood)
    
    
        
        
        