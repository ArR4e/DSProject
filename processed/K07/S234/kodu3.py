def sünnikuupäev (isikukood):
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if isikukood[0]=="1" or isikukood[0]=="2":
        sajand="18"
    elif isikukood[0]=="3" or isikukood[0]=="4":
        sajand="19"
    elif isikukood[0]=="5" or isikukood[0]=="6":
        sajand="20"
    elif isikukood[0]=="7" or isikukood[0]=="8":
        sajand="21"
    aasta="".join(isikukood[1:3])
    kuu="".join(isikukood[3:5])
    päev="".join(isikukood[5:7])
    vastus=päev+"."+" "+kuud[int(kuu)-1]+" "+sajand+aasta
    return vastus