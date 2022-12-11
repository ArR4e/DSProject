def moos(suur, väike, kogus):
    suurikulus = 0
    väikseidkulus = 0
    while suur > 0 and kogus <5:
        kogus -= 5
        suur -= 1
        suurikulus+= 1
    else:
        while väike > 0 and kogus >=1:
           kogus -= 1
           väike -= 1
           väikseidkulus += 1
        if kogus == 0:
            return(suurikulus+väikseidkulus)
        else:
            return(-1)
         
         
        
     
#moos(10,4,100)

