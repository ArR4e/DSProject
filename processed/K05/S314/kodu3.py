def moos(suur,väike,kogus):
    global karbid
    karbid = 0
    while suur > 0 and kogus - 5 >= 0:
           kogus -= 5
           suur -= 1
           karbid += 1
    while väike > 0 and kogus - 1 >= 0:
            kogus -= 1
            väike -= 1
            karbid += 1
    if kogus > 0:
        return -1
    if kogus <= 0:
        return karbid



