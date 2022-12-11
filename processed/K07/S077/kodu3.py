def sünnikuupäev(isikukood):
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    
    aastalõpp=isikukood[1:3]
    kuu=kuud[int(isikukood[3:5])-1]
    päev=isikukood[5:7]
    
    if int(isikukood[0]) in range(1,3):
        aastaalgus="18"
    if int(isikukood[0]) in range(3,5):
        aastaalgus="19"
    if int(isikukood[0]) in range(5,7):
        aastaalgus="20"
    
    return str(päev)+". "+str(kuu)+" "+aastaalgus+str(aastalõpp)
