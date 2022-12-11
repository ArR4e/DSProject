def sünnikuupäev(isikukood):
    numbrid=list(isikukood)
    if numbrid[3]+numbrid[4]=="01":
        kuu="jaanuar"
    elif numbrid[3]+numbrid[4]=="02":
        kuu="veebruar"
    elif numbrid[3]+numbrid[4]=="03":
        kuu="märts"
    elif numbrid[3]+numbrid[4]=="04":
        kuu="aprill"
    elif numbrid[3]+numbrid[4]=="05":
        kuu="mai"
    elif numbrid[3]+numbrid[4]=="06":
        kuu="juuni"
    elif numbrid[3]+numbrid[4]=="07":
        kuu="juuli"
    elif numbrid[3]+numbrid[4]=="08":
        kuu="august"
    elif numbrid[3]+numbrid[4]=="09":
        kuu="september"
    elif numbrid[3]+numbrid[4]=="10":
        kuu="oktoober"
    elif numbrid[3]+numbrid[4]=="11":
        kuu="november"
    elif numbrid[3]+numbrid[4]=="12":
        kuu="detsember"
        
            
    if numbrid[0]==str(5) or numbrid[0]==str(6):
        return(numbrid[5]+numbrid[6]+". "+kuu+ " "+ "20"+numbrid[1]+numbrid[2])
        
    if numbrid[0]==str(3) or numbrid[0]==str(4):
        return(numbrid[5]+numbrid[6]+". "+kuu+ " "+ "19"+numbrid[1]+numbrid[2])
    else:
        return(numbrid[5]+numbrid[6]+". "+kuu+ " "+ "18"+numbrid[1]+numbrid[2])
        
        
sünnikuupäev("50206290867")
