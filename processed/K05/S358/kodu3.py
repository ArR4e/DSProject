#kodu3

def moos(suured, vaiksed, moosi):
    if moosi > suured * 5 + vaiksed:
        return -1
    moosialg = moosi
    suurk = 0
    while moosi > 0 and suured > 0:
        moosi -= 5
        suurk += 1
        suured -= 1
    moosi += 5
    vk = 0
    while moosi > 0 and vaiksed > 0 and suurk*5+vk < moosialg:
        moosi -= 1
        vk += 1
        vaiksed -= 1
    return suurk + vk
