def moos(suur,väike,kogus):
    if kogus > suur*5 + väike:
        return(-1)
    elif kogus//5 <= suur and (kogus - (kogus//5)*5) <= väike :
        return((kogus//5) + (kogus-(kogus//5)*5))
    elif kogus//5 > suur and (kogus - suur*5) <= väike:
        return(suur + kogus-suur*5)
    elif kogus//5 <= suur and (kogus - (kogus//5)*5) > väike:
        return(-1)