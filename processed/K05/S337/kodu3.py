def moos(Sn, Vn, kg):
    a = kg//5 #mitmesse suurde karpi saab maksimaalselt moosi panna
    summa = 0
    if a <= Sn:
        summa = summa + a
        kg = kg - a*5
        if kg > Vn:
            return(-1)
        elif kg <= Vn:
            Vn = Vn - (Vn-kg)
            summa = summa + Vn
            return(summa)


    elif a > Sn:
        summa = summa + Sn
        kg = kg-Sn*5
        if kg > Vn:
            return(-1)
        elif kg <= Vn:
            Vn = Vn - (Vn-kg)
            summa = summa + Vn
            return(summa)
