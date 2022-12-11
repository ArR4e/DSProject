def moos(skarbid, vkarbid, kogus):
    skarbid = int(skarbid)
    vkarbid = int(vkarbid)
    kogus = int(kogus)
    karpidearv = 0
    while kogus > 0:
        while skarbid > 0:
            if kogus >= 5:
                kogus = kogus - 5
                karpidearv = karpidearv + 1
                skarbid = skarbid - 1
            else:
                break
        while vkarbid > 0:
            if kogus > 0:
                kogus = kogus - 1
                karpidearv = karpidearv + 1
                vkarbid = vkarbid - 1
            else:
                break
        if kogus > 0:
            karpidearv = -1
            break
    return karpidearv


