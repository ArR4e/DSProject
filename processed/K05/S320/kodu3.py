def moos(suur, väike, kogus):
    karpe=0
    while kogus > 0:
        if kogus >= 5 and suur > 0:
            suur -= 1
            kogus -= 5
        elif väike > 0:
            kogus -= 1
            väike -= 1
        else:
            return -1
        karpe += 1
    return karpe

suur=int(input("Sisesta suurte karpide arv:"))
väike=int(input("Sisesta väikeste karpide arv:"))
kogus=float(input("Sisesta keedetava moosi kogus:"))


print(moos(suur, väike, kogus))