def sünnikuupäev(isikukood):
    isikukood=list(str(isikukood))
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if int(isikukood[0])==3 or int(isikukood[0])==4:
        return isikukood[5].replace("0","")+isikukood[6]+". "+kuud[int(isikukood[3].replace("0","")+isikukood[4])-1]+" "+"19"+isikukood[1]+isikukood[2]
    elif int(isikukood[0])==1 or int(isikukood[0])==2:
        return isikukood[5].replace("0","")+isikukood[6]+". "+kuud[int(isikukood[3].replace("0","")+isikukood[4])-1]+" "+"18"+isikukood[1]+isikukood[2]
    else:
        return isikukood[5].replace("0","")+isikukood[6]+". "+kuud[int(isikukood[3].replace("0","")+isikukood[4])-1]+" "+"20"+isikukood[1]+isikukood[2]   