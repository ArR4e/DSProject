def moos(suur,väike,kogus):
    karbid = 0
    if kogus == 0:
        return 0
    for i in range(suur):
        kogus-=5
        karbid+=1
        if kogus == 0:
            return karbid
        if kogus <= 5:
            for i in range(väike):
                kogus-=1
                karbid+=1
                if kogus == 0:
                    return karbid
    for i in range(väike):
        kogus-=1
        karbid+=1
        if kogus == 0:
            return karbid
    return -1