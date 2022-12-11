def sünnikuupäev(isikukood):
    kuupäev=isikukood[5:7]
    kuu_nr=int(isikukood[3:5])
    kuude_järjend=["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu=kuude_järjend[kuu_nr-1]
    if int(isikukood[0])<=2:
        sajand="18"
    elif 2<int(isikukood[0])<=4:
        sajand="19"
    else:
        sajand="20"
    aasta=sajand+isikukood[1:3]
    
    return(kuupäev + ". " + kuu + " " + aasta)