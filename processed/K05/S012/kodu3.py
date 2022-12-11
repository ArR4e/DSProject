#kodu3 - moosi keetmine
#ska - suurte karpide arv
#vka - väikeste karpide arv
#kg - keedetud moosi kogus kilogrammides
def moos(ska, vka, kg):
    karpide_summa = 0
    s_karbid = 0
    while ska > 0 and kg >= 5:
        s_karbid = s_karbid + 1
        ska = ska-1
        kg=kg-5
    while vka >= kg and kg > 0:
        karpide_summa = s_karbid + kg
        vka = vka-kg
        kg = 0
    if vka < kg or kg < 0:
        return -1
    else:
        return karpide_summa
