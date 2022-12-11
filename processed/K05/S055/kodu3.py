def moos(suur, v2ike, kogus):
    _suur = int(kogus/5)
    karbid = 0
    if _suur <= suur:
        karbid += _suur
    else:
        karbid += suur
    _v2ike = kogus - karbid*5
    if v2ike >= _v2ike:
        return karbid + _v2ike
    else:
        return -1
