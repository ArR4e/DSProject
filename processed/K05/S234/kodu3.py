def moos(suur,vaike,kogus):
    if suur*5+vaike<kogus:
        return(-1)
    else:
        suuri=kogus//5 #Ideaalne suurte purkide kogus
        väikeseid=kogus-suuri*5 #Ideaalne väikeste purkide kogus
        if suuri<=suur and väikeseid<=vaike: #kas ideaalsete kogustega saab hakkam
            return(suuri+väikeseid)
        else:
            if väikeseid<=vaike: #Suurte purkide asemel lähevad kasutusele väikesed purgid
                väikeseid=kogus-suur*5 
                return(suur+väikeseid)
            else:
                return(-1)