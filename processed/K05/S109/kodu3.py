# s = suurte karpide arvu
# v = väikeste karpide arvu
# kg = keedetava moosi koguse kilogrammides

def moos(s, v, kg):
    i = 0
    while i < s and kg - 5 <= 5:
        i += 1
        if (kg - i*5) >= v:
            kõik = i + (kg - i*5)
            print(kõik)
        else:
            print(-1)
