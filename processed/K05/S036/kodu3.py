def moos(suur_karp,väike_karp,kogus):
    if kogus> (suur_karp*5+väike_karp):
        return -1
    else:
        i = 0
        while True:
            
            if kogus > 5:
                kogus -= 5*suur_karp
                i +=1*suur_karp
                if kogus < 0:
                    return -1
            else:
                if kogus == 0:
                    return i
                    break
                else:
                    kogus -=1*väike_karp
                    i += 1*väike_karp
                    if kogus < 0:
                        return -1
                    
moos(5,1,9)
