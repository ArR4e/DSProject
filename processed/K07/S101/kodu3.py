def sünnikuupäev(x):
    aasta=x[1:3]
    k=x[3:5]
    päev=x[5:7]
    while True:
        if x[0]=="3" or x[0]=="4":
            aasta="19"+aasta
            break
        elif x[0]=="1" or x[0]=="2":
            aasta="18"+aasta
            break
        elif x[0]=="5" or x[0]=="6":
            aasta="20"+aasta
            break
        elif x[0]=="7" or x[0]=="8":
            aasta="19"+aasta
            break
    while True:
        if k=="01":
            k="jaanuar"
            break
        elif k=="02":
            k="veebruar"
            break
        elif k=="03":
            k="märts"
            break
        elif k=="04":
            k="aprill"
            break
        elif k=="05":
            k="mai"
            break
        elif k=="06":
            k="juuni"
            break
        if k=="07":
            k="juuli"
            break
        elif k=="08":
            k="august"
            break
        elif k=="09":
            k="september"
            break
        elif k=="10":
            k="oktoober"
            break
        elif k=="11":
            k="november"
            break
        elif k=="12":
            k="detsember"
            break
        
        
            
    vastus= str(päev+". "+k+" "+aasta)
    return(vastus)