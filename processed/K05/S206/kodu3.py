def moos(suur, väike, kogus):
    i = 0
    if suur*5 + väike < kogus:
        return -1
    while kogus > 4 and suur > 0:
        kogus -= 5
        suur -= 1
        i += 1
    if kogus > väike:
        return -1
    while kogus > 0 and väike > 0:
        kogus -= 1
        väike -= 1
        i += 1
    return i


        