def sünnikuupäev(id):
    kood=[]
    if len(id) != 11:
        print("eh")
    elif len(id) == 11:
        for i in id:
            kood.append(i)
        päev=kood[5]+kood[6]
        if kood[0] == "3" or kood[0] == "4":
            aasta="19"+kood[1]+kood[2]
        elif kood[0] == "5" or kood[0] == "6":
            aasta="20"+kood[1]+kood[2]
        elif kood[0] == "1" or kood[0] == "2":
            aasta="18"+kood[1]+kood[2]
        if kood[3]+kood[4] == "01":
            kuu="jaanuar"
        elif kood[3]+kood[4] == "02":
            kuu="veebruar"
        elif kood[3]+kood[4] == "03":
            kuu="märts"
        elif kood[3]+kood[4] == "04":
            kuu="aprill"
        elif kood[3]+kood[4] == "05":
            kuu="mai"
        elif kood[3]+kood[4] == "06":
            kuu="juuni"
        elif kood[3]+kood[4] == "07":
            kuu="juuli"
        elif kood[3]+kood[4] == "08":
            kuu="august"
        elif kood[3]+kood[4] == "09":
            kuu="september"
        elif kood[3]+kood[4] == "10":
            kuu="oktoober"
        elif kood[3]+kood[4] == "11":
            kuu="november"
        elif kood[3]+kood[4] == "12":
            kuu="detsember"
    snp_kp=str(päev)+". "+str(kuu)+" "+str(aasta)
    return snp_kp