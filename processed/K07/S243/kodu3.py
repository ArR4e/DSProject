#sünnikuupäev isikukoodis

def sünnikuupäev(isikukood):
    aasta=int(isikukood[1:3])
    if aasta>21:
        aastaarv= "19" + str(aasta)
    if aasta<10:
        aastaarv= "200" + str(aasta)
    elif aasta<=21:
        aastaarv= "20" + str(aasta)
    kuu=isikukood[3:5]
    if kuu == "01":
        kuunimi= "jaanuar"
    elif kuu == "02":
        kuunimi="veebruar"
    elif kuu == "03":
        kuunimi="märts"
    elif kuu == "04":
        kuunimi="aprill"
    elif kuu == "05":
        kuunimi="mai"
    elif kuu == "06":
        kuunimi="juuni"
    elif kuu == "07":
        kuunimi="juuli"
    elif kuu == "08":
        kuunimi="august"
    elif kuu == "09":
        kuunimi="september"
    elif kuu == "10":
        kuunimi="oktoober"
    elif kuu == "11":
        kuunimi="november"
    elif kuu == "12":
        kuunimi="detsember"
    päev=isikukood[5:7]
    
    return str(päev) + ". " + kuunimi + " " + aastaarv

   