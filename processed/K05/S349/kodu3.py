def moos(suured_karbid, väiksed_karbid, kogus):
    if kogus >=5:
        if suured_karbid != 0:
            karbid = 0
            while kogus >= 5:
                kogus -= 5
                suured_karbid -= 1
                karbid += 1
        
                if suured_karbid == 0 and kogus > 0:
                    if väiksed_karbid != 0 and kogus > 0:
                        while kogus > 0:
                            kogus -= 1
                            väiksed_karbid -=1
                            karbid +=1
                    
                            if väiksed_karbid == 0 and kogus > 0:
                                return -1
                            else:
                                if väiksed_karbid != 0 and kogus == 0:
                                    return karbid
                        if kogus == 0:
                            return karbid
                    else:
                        if väiksed_karbid == 0 and kogus > 0:
                            return -1
                else:
                    if kogus == 0:
                        return karbid
                        
        else:
            if väiksed_karbid != 0 and kogus > 0:
                karbid = 0
                while kogus > 0:
                    kogus -= 1
                    väiksed_karbid -=1
                    karbid +=1
                    
                    if väiksed_karbid == 0 and kogus > 0:
                        return -1
                    else:
                        if väiksed_karbid != 0 and kogus == 0:
                            return karbid
            else:
                return -1
    else:
        if väiksed_karbid != 0 and kogus > 0:
           karbid = 0
           while kogus > 0:
                kogus -= 1
                väiksed_karbid -=1
                karbid +=1
                    
                if väiksed_karbid == 0 and kogus > 0:
                    return -1
                else:
                    if väiksed_karbid != 0 and kogus == 0:
                        return karbid
                    else:
                        return -1
        else:
            if suured_karbid > 0 and kogus < 5:
                karbid = 0
                while kogus < 5:
                    kogus -= 5
                    suured_karbid -= 1
                    karbid += 1
                    
                    if kogus == 0 or kogus <0:
                        return karbid
       

print(moos(1,0,3))

