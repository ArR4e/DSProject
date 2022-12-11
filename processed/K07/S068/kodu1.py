def poisse_ja_tüdrukuid(a):
    m=0
    n=0
    sõna=0
    for element in a:
        sõna=element.split()
        if sõna[-1]=="P":
            m+=1
        elif sõna[-1]=="T":
            n+=1
    
    return (m,n)
