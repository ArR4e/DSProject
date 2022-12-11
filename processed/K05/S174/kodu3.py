def moos(suured, väiksed, moosikogus):
    karpide_arv = 0
    #täisarvuline jagamine annab suurte karpide arvu, mida vaja
    vaj_suured = moosikogus // 5
    #kui vajaminevaid karpe on vähem või võrdne arv olemaolevatest karpidest,
    #siis saab Emma moosi teha
    if vaj_suured <= suured:
        karpide_arv += vaj_suured
        #jäägi leidmine annab meile väikeste karpide arvu, mida vaja
        vaj_väiksed = moosikogus % 5
        if vaj_väiksed <= väiksed:
            karpide_arv += vaj_väiksed
        else:
            return -1
    else:
        return -1
    return karpide_arv