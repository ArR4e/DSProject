def moos (suur, väike, kogus):
    karpe = 0
    suurk = 5
    väikek = 1
    kogusv = 0
    koguss = 0
    if kogus > 0:
        if  kogus % suurk == 0:
            karpe = kogus / suurk
            if karpe == suur:
                return int(karpe)
            elif karpe < suur:
                karpe = suur - karpe
                return int(karpe)
            elif karpe >= suur:
                kogusv = kogus-(suur*suurk)
                kogusv = kogusv/väikek
                if kogusv > väike:
                    return(-1)
                else:
                    karpe = suur+kogusv
                    return int(karpe)
            else:
                return(-1)
        elif (kogus // suurk*suur)>väike:
            return(-1)
        else:
            koguss = kogus // suurk
            if koguss <= suur:
                kogusv = kogus % suurk
                if kogusv <= väike: 
                    karpe = koguss + kogusv
                    return int(karpe)
                else:
                    return(-1)
            elif koguss > suur:
                #kogus = kogus-koguss
                kogusv = kogus/(väikek)
                
                if kogusv <= väike:
                    karpe = suur + kogusv
                    return int(karpe)
                else:
                    return(-1)
            else:
                return (-1)
    else:
        return(0)
moos(5,0,3)
