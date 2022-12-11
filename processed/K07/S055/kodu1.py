def poisse_ja_tüdrukuid(list):
    P, T = 0, 0
    for person in list:
        if person[-1] == "P":
            P += 1
        elif person[-1] == "T":
            T += 1
    return (P,T)
