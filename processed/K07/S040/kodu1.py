def poisse_ja_tüdrukuid(x):
    p = x[:]
    p_arv = 0
    t_arv = 0
    for rida in x:
        uus_rida = rida.split(" ")
        if uus_rida[-1] == "P":
            p_arv += 1
        elif uus_rida[-1] == "T":
            t_arv += 1
    return(p_arv, t_arv)
    print(poisse_ja_tüdrukuid)