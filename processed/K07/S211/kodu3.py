def sünnikuupäev(isikukood):
    
    kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
        
    sünd = list(isikukood)
    
    if int(sünd[0]) < 3:
        aasta = "18" + "".join(sünd[1:3])
        
    elif 2< int(sünd[0]) < 5:       
        aasta = "19" + "".join(sünd[1:3])
        
    elif 4 < int(sünd[0]) < 7:
        aasta = "20" + "".join(sünd[1:3])
        
    kuu_nr = "".join(sünd[3:5])
    kuu = kuud[(int(kuu_nr)-1)]
    päev = "".join(sünd[5:7])
    lause = [str(päev), '.', ' ', str(kuu), ' ', str(aasta)]
    tagastus = "".join(lause)

    return(tagastus)
