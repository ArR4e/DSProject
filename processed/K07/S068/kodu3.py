def sünnikuupäev(number):
    a=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    päev=0
    kuu=0
    aasta=0
    number=list(number)
    aasta = number[1]+number[2]
    kuu = number[3]+number[4]
    päev=number[5]+number[6]
    
    if number[0]=="3" or number[0]=="4":
        aasta= str("19") + str(aasta)
    elif number[0]=="5" or number[0]=="6":
        aasta=str("20")+str(aasta)
    elif number[0]=="1" or number[0]=="2":
        aasta=str("18")+str(aasta)
        
    kuu=int(kuu)   
    kuu= a[kuu-1]
    päev=str(päev)
    
    return(str(päev)+". " +str(kuu)+" "+ str(aasta))
    
    
