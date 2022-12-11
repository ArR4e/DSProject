def maksuvabatulu(palk):
    if palk <= 6000:
        return print("Maksuvaba tulu on " + round(palk,2) + " eurot")
    elif palk > 6000 and palk <= 14400:
        print("Maksuvaba tulu on 6000 eurot")
    elif palk > 14400 and palk <= 25200:
        return print("Maksuvaba tulu on " + str(round(6000-6000/10800*(palk-14400),2)) + " eurot")
    else:
        return print("Maksuvaba tulu on 0 eurot")

aasta_palk = float(input("Sisesta aastatulu: "))
maksuvabatulu(aasta_palk)