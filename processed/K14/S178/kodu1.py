def rek_abs(järjend):
    vastus = []
    lõpp = []
    for rida in järjend:
        if isinstance(rida, list) == True:
            vastus.append(rek_abs(rida))
        else:
            aelement = abs(rida)
            vastus.append(aelement)

    return(vastus)


print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))