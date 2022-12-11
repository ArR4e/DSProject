def sünnikuupäev(kood):
    mapped=map(int,str(kood))
    eraldi=list(mapped)
    if eraldi[0]==5 or eraldi[0]==6:
        aasta1="20"
    elif eraldi[0]==3 or eraldi[0]==4:
        aasta1="19"
    elif eraldi[0]==1 or eraldi[0]==2:
        aasta1="18"
    aasta2=str(eraldi[1])+str(eraldi[2])
    if eraldi[3]==0:
        if eraldi[4]==1:
            kuu="jaanuar"
        elif eraldi[4]==2:
            kuu="veebruar"
        elif eraldi[4]==3:
            kuu="märts"
        elif eraldi[4]==4:
            kuu="aprill"
        elif eraldi[4]==5:
            kuu="mai"
        elif eraldi[4]==6:
            kuu="juuni"
        elif eraldi[4]==7:
            kuu="juuli"
        elif eraldi[4]==8:
            kuu="august"
        elif eraldi[4]==9:
            kuu="september"
    elif eraldi[3]==1:
        if eraldi[4]==0:
            kuu="oktoober"
        elif eraldi[4]==1:
            kuu="november"
        elif eraldi[4]==2:
            kuu="detsember"
    if int(str(eraldi[5])+str(eraldi[6]))<32 and int(str(eraldi[5])+str(eraldi[6]))>0:
        if eraldi[5]==0:
            päev=str(eraldi[6])
        else:
            päev=str(eraldi[5])+str(eraldi[6])
    return str(päev+". "+kuu+" "+aasta1+aasta2)