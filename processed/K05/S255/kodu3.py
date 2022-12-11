def moos(suur, vaike, kogus_kg):
    karpide_arv = 0
    while True:
        if kogus_kg >= 5 and suur > 0:
            karpide_arv += 1
            kogus_kg -= 5
            suur -= 1
        elif kogus_kg >= 1 and vaike > 0:
            karpide_arv += 1
            kogus_kg -= 1
            vaike -= 1
        elif karpide_arv == 0 and kogus_kg == 0:
            return(0)
        else:
            return(-1)
        if suur == 0 and vaike == 0 and kogus_kg > 0:
            return(-1)
        if kogus_kg == 0:
            break
    return(karpide_arv)
print(moos(4, 3, 0))