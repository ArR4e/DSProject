#poiste ja tydrukute arv

#x = ["Mati P", "Kati T", "Siim Aleksander P", "Jüri P", "Veronika T"]   
def poisse_ja_tüdrukuid(x):
    y = x.copy()
    def p1kkus():
        i = 0
        while i < 1:
            d = len(y.pop(i))
            i += 1
        s = int(d-1)
        return d  
    #print(poisse_ja_tüdrukuid(x))

    def t2ht():
        list = []
        for i in x:
            for i2 in i:
                list.append(i2)
        return list

    täht = t2ht().copy()
    #pikkus = p1kkus()
    def st():
        i = 0
        d1 = p1kkus()
        while i < d1:
            d= täht.pop(0)
            i += 1
        s = d
        return s

    i = 0
    poiss = []
    tydruk = []
    while i < len(x):
        d = st()
        if d == "P":
            poiss.append(1)
        if d == "T":
            tydruk.append(1)
        i += 1
    p_arv = sum(poiss)
    t_arv = sum(tydruk)

    ennik = (p_arv, t_arv)
    
    return ennik
