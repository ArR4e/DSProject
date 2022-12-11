

def moos(suurKarp,väikeKarp,moos):
    kokkuSuuri = suurKarp
    kokkuVäikseid = väikeKarp
    while moos > 0:
        if moos // 5 > 0 and suurKarp > 0:
            moos -= 5
            suurKarp-=1
        elif väikeKarp > 0:
            moos -= 1
            väikeKarp -= 1
        else:
            return -1
    return (kokkuSuuri-suurKarp + kokkuVäikseid-väikeKarp)

print(moos(8,5,44))
            