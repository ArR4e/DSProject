def poisse_ja_tüdrukuid(jär):
    p=0
    t=0
    for el in jär:
        if el[(len(el))-1] == "P":
            p+=1
        if el[(len(el))-1] == "T":
            t+=1
    return (p, t)

