def sünnikuupäev(a):
    aasta=""
    kuu=""
    p2ev=""
    kood=[]
    kuud=["","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    for char in a:
        kood.append(char)
    aasta=kood[1]+kood[2]
    if kood[3]=="0":
        kuu=kood[4]
        kuu=int(kuu)
    else:
        kuu=kood[3]+kood[4]
        kuu=int(kuu)
    p2ev=kood[5]+kood[6]
    if int(kood[0])==1 or int(kood[0])==2:
        return(p2ev+". "+kuud[kuu]+" 18"+aasta)
    if int(kood[0])==3 or int(kood[0])==4:
        return(p2ev+". "+kuud[kuu]+" 19"+aasta)
    if int(kood[0])==5 or int(kood[0])==6:
        return(p2ev+". "+kuud[kuu]+" 20"+aasta)
    if int(kood[0])==7 or int(kood[0])==8:
        return(p2ev+". "+kuud[kuu]+" 21"+aasta)
    