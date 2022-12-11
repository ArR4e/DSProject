def rek_abs(jär):
    uus = []
    if jär == []:
        return jär
    for i in range(len(jär)):
        if isinstance(jär[i],list):
            uus += [rek_abs(jär[i])]
        else:
            uus += [abs(jär[i])]
    return uus
print(rek_abs([2, -6,[8,-12,[-12]],8,[]]))