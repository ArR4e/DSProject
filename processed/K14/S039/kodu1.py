def rek_abs(jär):
    x=0
    if isinstance(jär,list):
        uus_jär=jär[:]
        for el in jär:
            el=rek_abs(el)
            uus_jär[x]=el
            x+=1
        return uus_jär
    else:
        jär=abs(jär)
        return jär
