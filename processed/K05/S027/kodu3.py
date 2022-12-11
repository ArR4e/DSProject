def moos(suur, väike, kogus):
    a = 5*suur
    b = väike
    karp = 0
    if a + b < kogus or kogus - a > b:
        return -1
    elif kogus - a == 0:
        return suur
    while kogus - a < 0:
        suur -= 1
        a = 5*suur
    kogus -= a
    karp += suur
    if kogus > b:
        return -1
    elif kogus - b == 0:
        return suur + väike
    elif kogus < b:
        return karp + kogus