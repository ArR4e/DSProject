suured = int(input("Sisesta suurte karpide arv: "))
väiksed = int(input("Sisesta väikeste karpide arv: "))
kogus = int(input("Sisesta moosi kogus kilogrammides: "))

def moos(suured, väiksed, kogus):
    if (suured * 5 + väiksed * 1) < kogus:
        return -1
    else:
        #suurte kogus
        x = (kogus // 5)
        #väikeste kogus
        y = (kogus - x*5) // 1
        if x > suured or y > väiksed:
            return -1
        else:
            return x + y

print(moos(suured, väiksed, kogus))