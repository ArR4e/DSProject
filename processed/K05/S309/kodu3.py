def moos(bigcount, smallcount, jamamount):
    
    #viskame kohe -1 vastuseks kui karpide mahutuvuse summa on väiksem kui moosi kogus
    if((bigcount*5 + smallcount) < jamamount):
        return -1

    #leiame mitut suurt karpi me saaks maksimaalselt kasutada
    big = jamamount // 5

    #kuid kui leitud maksimaalne karpide arv on suurem kui olemasolev viiekiloste karpide arv,
    #seame olemasolevate karpide arvu selleks karpide arvuks, mida kasutame
    if(big > bigcount):
        big = bigcount

    #leiame mitu väikest karpi on vaja et koos suurtega, mahutada ära moos
    small = (jamamount - big*5)

    #kui meil on piisavalt väikeseid karpe, et ülejäänud moos ära mahutada, tagastame kasutajale
    #väikeste ja suurte karpide summa
    if(smallcount >= small):
        return (big + small)
    else:
        return -1