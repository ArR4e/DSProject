def moos(suur,vaike,kogus):
    kokku = 0
    if kogus - (5*suur + vaike) > 0:
        return -1
    while suur > 0 and kogus >= 5:
        kokku += 1
        suur -= 1
        kogus -= 5
    while vaike > 0 and kogus > 0:
        kokku += 1
        vaike -= 1
        kogus -= 1
    if kogus > 0:
        return -1
    return int(kokku)
        
print(moos(1,0,5))
