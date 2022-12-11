isikukood="34501234215"
def sünnikuupäev(isikukood):
    sünd=""
    päev=int(isikukood[5:7])
    sünd+=str(päev)+". "
    kuu=isikukood[3:5]
    if kuu=="01":
        sünd+="jaanuar"
    elif kuu=="02":
        sünd+="veebruar"
    elif kuu=="03":
        sünd+="märts"
    elif kuu=="04":
        sünd+="aprill"
    elif kuu=="05":
        sünd+="mai"
    elif kuu=="06":
        sünd+="juuni"
    elif kuu=="07":
        sünd+="juuli"
    elif kuu=="08":
        sünd+="august"
    elif kuu=="09":
        sünd+="september"
    elif kuu=="10":
        sünd+="oktoober"
    elif kuu=="11":
        sünd+="november"
    elif kuu=="12":
        sünd+="detsember"

    sajand=int(isikukood[0])
    if sajand==3 or sajand==4:
        sünd+=" 19"
    elif sajand==5 or sajand==6:
        sünd+=" 20"
    elif sajand==1 or sajand==2:
        sünd+=" 18"
    aasta=isikukood[1:3]
    sünd+=aasta
        
    return sünd

print(sünnikuupäev(isikukood))