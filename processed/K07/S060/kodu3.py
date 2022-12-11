def sünnikuupäev(arv): #Võibolla saab kuidagi ilusamalt
    aasta=0
    kuu=0
    if int(arv[0])==1 or int(arv[0])==2:
        aasta=1800+int(arv[1])*10+int(arv[2])*1
    elif int(arv[0])==3 or int(arv[0])==4:
        aasta=1900+int(arv[1])*10+int(arv[2])*1
    elif int(arv[0])==5 or int(arv[0])==6:
        aasta=2000+int(arv[1])*10+int(arv[2])*1
    if int(arv[3])==0 and int(arv[4])==1:
        kuu="jaanuar"
    elif int(arv[3])==0 and int(arv[4])==2:
        kuu="veebruar"
    elif int(arv[3])==0 and int(arv[4])==3:
        kuu="märts"
    elif int(arv[3])==0 and int(arv[4])==4:
        kuu="aprill"
    elif int(arv[3])==0 and int(arv[4])==5:
        kuu="mai"
    elif int(arv[3])==0 and int(arv[4])==6:
        kuu="juuni"
    elif int(arv[3])==0 and int(arv[4])==7:
        kuu="juuli"
    elif int(arv[3])==0 and int(arv[4])==8:
        kuu="august"
    elif int(arv[3])==0 and int(arv[4])==9:
        kuu="september"
    elif int(arv[3])==1 and int(arv[4])==0:
        kuu="oktoober"
    elif int(arv[3])==1 and int(arv[4])==1:
        kuu="november"
    elif int(arv[3])==1 and int(arv[4])==2:
        kuu="detsember"
    päev=int(arv[5])*10+int(arv[6])
        
    return (str(päev)+". "+kuu+" "+str(aasta))
