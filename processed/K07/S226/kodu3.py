eesti_id = "60101017683"
kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    kuu = int(kuu) #lol
    kuu_nimi = kuude_järjend[kuu-1]
    
    if isikukood[0] == "3" or isikukood[0] == "4":
        aasta = "19" + isikukood[1:3] 
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta = "20" + isikukood[1:3]
    sünnikuupäev = päev + ". " + kuu_nimi + " " + aasta
    return sünnikuupäev
        

print(sünnikuupäev(eesti_id))



# print(aasta, kuu, päev)


#23. jaanuar 1945

# 
# 
# päeva_nr = 7
# päevade_järjend = ["esmaspäev","teisipäev", "kolmapäev", "neljapäev", "reede", "laupäev","pühapäev"]
# päeva_nimi = päevade_järjend[päeva_nr-1]
# print(päeva_nimi)
# def sünnikuupäev(isikukood):
# aasta = eesti_id[1:3]
# kuu = eesti_id[3:5]
# päev = eesti_id[5:7]
# print(eesti_id[0])
