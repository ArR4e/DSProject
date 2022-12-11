def moos(suur, väike, kogus):
    kokku = 0
    while suur > 0 and kogus - 5 >= 0:
        kokku += 1
        kogus -= 5
        suur -= 1
    while väike > 0 and kogus > 0:
        kokku += 1
        kogus -= 1
        väike -= 1
    if suur >= 0 and väike >= 0 and kogus == 0:
        return(kokku)
    else:
        return(-1)