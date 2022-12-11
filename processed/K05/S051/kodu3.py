def moos(suured_karbid, väiksed_karbid, kogus):
    karbid_kokku = 0
    while True:
        if kogus - 5 >= 0 and suured_karbid > 0:
            suured_karbid -= 1
            kogus -= 5
            karbid_kokku += 1
            continue
        elif kogus - 1 >= 0 and väiksed_karbid > 0:
            väiksed_karbid -= 1
            kogus -= 1
            karbid_kokku += 1
            continue
        elif kogus == 0:
            break
        else:
            karbid_kokku = -1
            break
    return karbid_kokku