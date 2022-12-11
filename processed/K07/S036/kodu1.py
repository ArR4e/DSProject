def poisse_ja_tüdrukuid(lst):
    poisse = 0
    tüdrukuid = 0
    for i in lst:
        if i[-1]=="P":
            poisse += 1
        elif i[-1]=="T":
            tüdrukuid +=1
        else:
            continue
    return (poisse,tüdrukuid)

poisse_ja_tüdrukuid(['Mari T', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
