kuud=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
isikukood='39910122345'
def sünnikuupäev(isikukood):
    järj = [int(a) for a in str(isikukood)]
    if järj[0]==1 or järj[0]==2:
        aasta=1800+järj[1]*10+järj[2]
    elif järj[0]==3 or järj[0]==4:
        aasta=1900+järj[1]*10+järj[2]
    elif järj[0]==5 or järj[0]==6:
        aasta=2000+järj[1]*10+järj[2]
    if järj[3]==0:
        kuu=kuud[järj[4]-1]
    else:
        kuu=kuud[10+järj[4]-1]
    if järj[5]==0:
        päev=järj[6]
    else:
        päev=järj[5]*10+järj[6]
    lause= (str(päev) + ". " + kuu + " "+ str(aasta))
    return lause
print(sünnikuupäev(isikukood))