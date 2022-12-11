isikukood = input()
kuude_list = [" ","jaanuar", "veebruar", "märts",
              "aprill", "mai", "juuni", "juuli",
              "august", "september", "oktoober",
              "november", "detsember"]
def sünnikuupäev(isikukood):
    kuupäev = isikukood[5:7]
    
    if isikukood[3:4] == "0":
        kuu = isikukood[4:5]
    else:
        kuu = isikukood[3:5]
    
    kuu_sõnana = kuude_list[int(kuu)]

    if isikukood[0] == "1" or isikukood[0] == "2":
        sajand = "18" + isikukood[1:3]
    elif isikukood[0] == "3" or isikukood[0] == "4":
        sajand = "19" + isikukood[1:3]
    else:
        sajand = "20" + isikukood[1:3]

    return(kuupäev + ". " + kuu_sõnana + " "+ sajand)

print(sünnikuupäev(isikukood))
    